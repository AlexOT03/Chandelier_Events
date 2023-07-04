from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from chandelier_events.apps.admin.quote.models import Quote

# Create your views here.
class quotePageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        quotes = Quote.objects.all()
        
        return render(request, 'quote.html', {
            'quotes': quotes,
        })
    
    def post(self, request, *args, **kwargs):
        return redirect('quote_admin')
    
    def show(self, request, id, **kwargs):
        quote = Quote.objects.get(id=id)
        
        return render(request, 'quote_info.html', {
            'quote': quote,
        })
    
    def update(self, request, *args, **kwargs):
        return redirect('quote_admin')
    
    def delete(self, request, id, **kwargs):
        quote = Quote.objects.get(id=id)
        quote.delete()
        
        return redirect('quote_admin')