from django.shortcuts import render
from django.views import View
from chandelier_events.apps.admin.quote.models import Quote
from chandelier_events.apps.admin.quote.form import QuotesForm

# Create your views here.
class homePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
    def post(self, request, *args, **kwargs):
        return render(request, '')
    
    def show(self, request, *args, **kwargs):
        return render(request, '')
    
    def update(self, request, *args, **kwargs):
        return render(request, '')
    
    def delete(self, request, *args, **kwargs):
        return render(request, '')
    
class fastquotePageView(View):
    def get(self, request, *args, **kwargs):
        form_quote = QuotesForm()
        return render(request, 'fast_quote.html', {
            'form_quote': form_quote,
        })
    
    def post(self, request, *args, **kwargs):
        return render(request, '')
    
    def show(self, request, *args, **kwargs):
        return render(request, '')
    
    def update(self, request, *args, **kwargs):
        return render(request, '')
    
    def delete(self, request, *args, **kwargs):
        return render(request, '')

class locationPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'location.html')
    
    def post(self, request, *args, **kwargs):
        return render(request, '')
    
    def show(self, request, *args, **kwargs):
        return render(request, 'location_info.html')
    
    def update(self, request, *args, **kwargs):
        return render(request, '')
    
    def delete(self, request, *args, **kwargs):
        return render(request, '')

class aboutPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about_us.html')
    
    def post(self, request, *args, **kwargs):
        return render(request, '')
    
    def show(self, request, *args, **kwargs):
        return render(request, '')
    
    def update(self, request, *args, **kwargs):
        return render(request, '')
    
    def delete(self, request, *args, **kwargs):
        return render(request, '')