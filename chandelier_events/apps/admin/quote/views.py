from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from chandelier_events.apps.admin.quote.models import Quote
from chandelier_events.apps.admin.location.models import Location
from chandelier_events.apps.admin.quote_pdf.models import QuoteDetail
from num2words import num2words
from datetime import datetime, timedelta

# Create your views here.
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

class quotePageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        quotes = Quote.objects.all()
        quotes_details = QuoteDetail.objects.all()

        for quote in quotes:
            for quote_detail in quotes_details:
                if quote_detail.quote.id == quote.id:
                    quote.is_on = True
                    quote.on_date = quote_detail.update_date

        return render(request, 'quote.html', {
            'quotes': quotes,
            'quotes_details': quotes_details,
        })
        
    def show(self, request, id, **kwargs):
        quote = Quote.objects.get(id=id)
        total_price = 0
        total_price_text =""
        
        try:
            quote_details = QuoteDetail.objects.get(quote=quote)
            sub_total = (quote.total_service + quote_details.transport) - quote_details.discount
            iva_total = round(sub_total * quote_details.iva, 2)
            
            if quote.location != None:
                location = Location.objects.get(id=quote.location.id)
                total_hours =get_time(quote.start_time, quote.end_time)
                location_price = location.price * int(total_hours)

                total_price = location_price + sub_total + iva_total
                total_price_text = num2words(total_price, lang='es').title()
            else:
                sub_total = (quote.total_service + quote_details.transport) - quote_details.discount
                iva_total = round(sub_total * quote_details.iva, 2)
                total_price = sub_total + iva_total
                total_price_text = num2words(total_price, lang='es').title()
            
        except QuoteDetail.DoesNotExist:
            quote_details = None
            

        total_text = num2words(quote.total_service, lang='es').title()
        
        return render(request, 'quote_info.html', {
            'quote': quote,
            'quote_details': quote_details,
            'total_text': total_text,
            'total_price': total_price,
            'total_price_text': total_price_text,
        })
    
    def delete(self, request, id, **kwargs):
        quote = Quote.objects.get(id=id)
        quote.delete()
        
        return redirect('quote_admin')