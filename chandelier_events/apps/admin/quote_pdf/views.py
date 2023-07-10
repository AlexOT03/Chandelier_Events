from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from chandelier_events.apps.admin.quote.models import Quote
from chandelier_events.apps.admin.service.models import Service, ServiceDetail
from chandelier_events.apps.admin.quote_pdf.form import QuoteDetailsForm
from chandelier_events.apps.admin.quote_pdf.models import QuoteDetail
import uuid

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from num2words import num2words

# Create your views here.
class QuoteDetailView(LoginRequiredMixin, View):
    def get(self, request, id, **kwargs):
        quote = Quote.objects.get(id=id)
        total_text = num2words(quote.total_service, lang='es').title()
        form_quote_details = QuoteDetailsForm()
        
        return render(request, 'quote_pdf_form.html', {
            'quote': quote,
            'total_text': total_text,
            'form_quote_details': form_quote_details,
        })
        
    def post(self, request, id, *args, **kwargs):
        quote = Quote.objects.get(id=id)
        total_text = num2words(quote.total_service, lang='es').title()
        form_quote_details = QuoteDetailsForm(request.POST)
        
        if form_quote_details.is_valid():
            quote_details = form_quote_details.save(commit=False)
            quote_details.folio = uuid.uuid4()
            quote_details.quote = quote
            quote_details.save()
            
            return redirect("quote_admin")
        
        return render(request, 'quote_pdf_form.html', {
            'quote': quote,
            'total_text': total_text,
            'form_quote_details': form_quote_details,
        })

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class ViewPDF(LoginRequiredMixin, View):
    def get(self, request, id, **kwargs):
        quote = Quote.objects.get(id=id)
        quote_details = QuoteDetail.objects.get(quote=quote)
        
        service_details = quote.service_detail.all()
        service_details_list = list(service_details)
        
        sub_total = (quote.total_service + quote_details.transport) - quote_details.discount
        iva_total = round(sub_total * quote_details.iva, 2)
        
        total_price = sub_total + iva_total
        total_price_words = num2words(total_price, lang='es').title()
        
        name_pdf = "Cotizacion para " + str(quote.theme) + ", Num." + str(quote.id)
        
        data = {
            "pdf_title": name_pdf,
            "created_day": quote_details.update_date,
            "send_day": quote.created_date,
            "quote_folio": quote_details.folio,
            "name": quote.name,
            "last_name": quote.last_name,
            "email": quote.email,
            "phone": quote.phone,
            "services_list": service_details_list,
            "services_total_price": quote.total_service,
            "theme_event": quote.theme,
            "day_of_event": quote.date_of_event,
            "start_time": quote.start_time,
            "end_time": quote.end_time,
            "people": quote.people,
            "discount": quote_details.discount,
            "sub_total":"",
            "transport": quote_details.transport,
            "iva_number": quote_details.get_iva_display,
            "iva_price": iva_total,
            "total_price": total_price,
            "total_price_words": total_price_words,
            "client_observations": quote.message,
            "observations": quote_details.message,
            "user_name": quote_details.name,
        }
        
        pdf = render_to_pdf('pdf/quote_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    
class DownloadPDF(LoginRequiredMixin, View):
    def get(self, request, id, **kwargs):
        quote = Quote.objects.get(id=id)
        quote_details = QuoteDetail.objects.get(quote=quote)
        
        service_details = quote.service_detail.all()
        service_details_list = list(service_details)
        
        sub_total = (quote.total_service + quote_details.transport) - quote_details.discount
        iva_total = round(sub_total * quote_details.iva, 2)
        
        total_price = sub_total + iva_total
        total_price_words = num2words(total_price, lang='es').title()
        
        name_pdf = "Cotizacion para " + str(quote.theme) + ", Num." + str(quote.id)
        
        data = {
            "pdf_title": name_pdf,
            "created_day": quote_details.update_date,
            "send_day": quote.created_date,
            "quote_folio":"",
            "name": quote.name,
            "last_name": quote.last_name,
            "email": quote.email,
            "phone": quote.phone,
            "services_list": service_details_list,
            "services_total_price": quote.total_service,
            "theme_event": quote.theme,
            "day_of_event": quote.date_of_event,
            "start_time": quote.start_time,
            "end_time": quote.end_time,
            "people": quote.people,
            "discount": quote_details.discount,
            "sub_total":"",
            "transport": quote_details.transport,
            "iva_number": quote_details.get_iva_display,
            "iva_price": iva_total,
            "total_price": total_price,
            "total_price_words": total_price_words,
            "client_observations": quote.message,
            "observations": quote_details.message,
        }
        
        pdf = render_to_pdf('pdf/quote_pdf.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "attachment; filename='%s" %(filename)
        response['Content-Disposition'] = content
        
        return response