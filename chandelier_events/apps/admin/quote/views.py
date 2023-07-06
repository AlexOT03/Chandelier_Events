from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from chandelier_events.apps.admin.quote.models import Quote
from num2words import num2words

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
# from .views import View
from xhtml2pdf import pisa

# Create your views here.
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class quotePageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        quotes = Quote.objects.all()
        
        return render(request, 'quote.html', {
            'quotes': quotes,
        })
        
    def show(self, request, id, **kwargs):
        quote = Quote.objects.get(id=id)
        total_text = num2words(quote.total_service, lang='es')
        
        return render(request, 'quote_info.html', {
            'quote': quote,
            'total_text': total_text,
        })
    
    def delete(self, request, id, **kwargs):
        quote = Quote.objects.get(id=id)
        quote.delete()
        
        redirect('quote_admin')
        
class ViewPDF(LoginRequiredMixin, View):
    def get(self, request, id, **kwargs):
        
        data = {
            "name": "prueba",
            "last_name": "render",
            "date": "01/02/2003",
            "id_quote":"had921b1bui1",
            "address":"none",
            "phone":"9933445566",
            "email":"example@example.com",
            "city":"Tabasco",
            "tematica":"boda",
            "dia_evento":"01/11/2022",
            "hora_inicio":"11am",
            "hora_fin":"7pm",
            "otros":"none",
            "total_bruto":"500",
            "descuento":"0",
            "sub_total":"520",
            "transporte":"300",
            "iva":"200",
            "total_final":"10,234",
            "observaciones":"Prueb de creacion de pdf",
        }
        
        pdf = render_to_pdf('pdf/base_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    
class DownloadPDF(LoginRequiredMixin, View):
    def get(self, request, id, **kwargs):
        
        data = {
            "name": "prueba",
            "last_name": "render",
            "date": "01/02/2003",
            "id_quote":"had921b1bui1",
            "address":"none",
            "phone":"9933445566",
            "email":"example@example.com",
            "city":"Tabasco",
            "tematica":"boda",
            "dia_evento":"01/11/2022",
            "hora_inicio":"11am",
            "hora_fin":"7pm",
            "otros":"none",
            "total_bruto":"500",
            "descuento":"0",
            "sub_total":"520",
            "transporte":"300",
            "iva":"200",
            "total_final":"10,234",
            "observaciones":"Prueb de creacion de pdf",
        }
        
        pdf = render_to_pdf('pdf/base_pdf.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "attachment; filename='%s" %(filename)
        response['Content-Disposition'] = content
        
        return response
        