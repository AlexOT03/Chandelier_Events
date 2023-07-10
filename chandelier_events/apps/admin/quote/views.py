from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from chandelier_events.apps.admin.quote.models import Quote
from chandelier_events.apps.admin.quote_pdf.models import QuoteDetail
from num2words import num2words

# Create your views here.
class quotePageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        quotes = Quote.objects.all()
        
        return render(request, 'quote.html', {
            'quotes': quotes,
        })
        
    def show(self, request, id, **kwargs):
        quote = Quote.objects.get(id=id)
        quote_details = QuoteDetail.objects.get(quote=quote)
        # quote = Quote.objects.get(id=id)
        # quote_details = QuoteDetail.objects.filter(quote=quote)
        
        total_text = num2words(quote.total_service, lang='es').title()
        
        return render(request, 'quote_info.html', {
            'quote': quote,
            'quote_details': quote_details,
            'total_text': total_text,
        })
    
    def delete(self, request, id, **kwargs):
        quote = Quote.objects.get(id=id)
        quote.delete()
        
        return redirect('quote_admin')