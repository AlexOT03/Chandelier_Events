from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from chandelier_events.apps.admin.quote.models import Quote
from chandelier_events.apps.admin.service.models import Service, ServiceDetail
from chandelier_events.apps.admin.location.models import Location
from chandelier_events.apps.admin.quote_pdf.form import QuoteDetailsForm
from chandelier_events.apps.admin.quote_pdf.models import QuoteDetail
import uuid
import string

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from num2words import num2words

from datetime import datetime, timedelta

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
        
    def update(self, request, id, **kwargs):
        quote = Quote.objects.get(id=id)
        total_text = num2words(quote.total_service, lang='es').title()
        quote_details = QuoteDetail.objects.get(quote=quote)
        
        if request.method == 'POST':
            form_quote_details = QuoteDetailsForm(request.POST, instance=quote_details)
            if form_quote_details.is_valid():
                form_quote_details.save()
      
                return redirect("quote_admin")
        else:
            form_quote_details = QuoteDetailsForm(instance=quote_details)
        
        return render(request, 'quote_pdf_edit.html', {
            'quote': quote,
            'total_text': total_text,
            'form_quote_details': form_quote_details,
        })

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def get_time(start, end):
    current_date = datetime.now().date()

    start_datetime = datetime.combine(current_date, start)
    end_datetime = datetime.combine(current_date, end)

    if end_datetime < start_datetime:
        # Si es así, agregar un día a la fecha de finalización
        end_datetime += timedelta(days=1)

    # Calcular la diferencia de tiempo
    time_difference = end_datetime - start_datetime

    # Obtener el número de horas
    hours = time_difference.total_seconds() // 3600
    
    return hours

class ViewPDF(LoginRequiredMixin, View):
    def get(self, request, id, **kwargs):
        quote = Quote.objects.get(id=id)
        quote_details = QuoteDetail.objects.get(quote=quote)
        
        location = None
        hour_price = None
        total_hours = 0
        location_price = None
        
        try:
            if quote.location != None:
                location = Location.objects.get(id=quote.location.id)
                hour_price = location.price
                total_hours =get_time(quote.start_time, quote.end_time)
                location_price = location.price * int(total_hours)
            
        except Location.DoesNotExist:
            location = None
            location_price = None
        
        
        service_details = quote.service_detail.all()
        service_details_list = list(service_details)
        
        sub_total = (quote.total_service + quote_details.transport) - quote_details.discount
        iva_total = round(sub_total * quote_details.iva, 2)
        
        if location != None and location_price != None:
            total_price = sub_total + iva_total + location_price
        else:
            total_price = sub_total + iva_total
            
        total_price_words = num2words(total_price, lang='es').title()
        
        name_pdf = ""
        if quote.theme == None:
            name_pdf = "Cotizacion libre, Num." + str(quote.id)
        else:
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
            "location_price": location_price,
            "total_hours": total_hours,
            "hour_price": hour_price,
            "start_time": quote.start_time,
            "end_time": quote.end_time,
            "people": quote.people,
            "location": quote.location,
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
        
        # service_details = quote.service_detail.all()
        # service_details_list = list(service_details)
        
        # sub_total = (quote.total_service + quote_details.transport) - quote_details.discount
        # iva_total = round(sub_total * quote_details.iva, 2)
        
        # total_price = sub_total + iva_total
        location = None
        hour_price = None
        total_hours = 0
        location_price = None
        
        try:
            if quote.location != None:
                location = Location.objects.get(id=quote.location.id)
                hour_price = location.price
                total_hours =get_time(quote.start_time, quote.end_time)
                location_price = location.price * int(total_hours)
            
        except Location.DoesNotExist:
            location = None
            location_price = None
        
        
        service_details = quote.service_detail.all()
        service_details_list = list(service_details)
        
        sub_total = (quote.total_service + quote_details.transport) - quote_details.discount
        iva_total = round(sub_total * quote_details.iva, 2)
        
        if location != None and location_price != None:
            total_price = sub_total + iva_total + location_price
        else:
            total_price = sub_total + iva_total
            
        total_price_words = num2words(total_price, lang='es').title()
        
        name_pdf = ""
        if quote.theme == None:
            name_pdf = "Cotizacion libre, Num." + str(quote.id)
        else:
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
            "location_price": location_price,
            "total_hours": total_hours,
            "hour_price": hour_price,
            "start_time": quote.start_time,
            "end_time": quote.end_time,
            "people": quote.people,
            "location": quote.location,
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
        response = HttpResponse(pdf, content_type='application/pdf')
        pdf_filename = "Cotizacion para " + quote.name + " " + quote.last_name
        filename = "%s.pdf" %(pdf_filename)
        content = "attachment; filename='%s" %(filename)
        response['Content-Disposition'] = content
        
        return response