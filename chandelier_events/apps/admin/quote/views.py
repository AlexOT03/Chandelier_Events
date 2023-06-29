from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class quotePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quote.html')
    
    def post(self, request, *args, **kwargs):
        return redirect('quote_admin')
    
    def show(self, request, *args, **kwargs):
        return render(request, 'quote_info.html')
    
    def update(self, request, *args, **kwargs):
        return redirect('quote_admin')
    
    def delete(self, request, *args, **kwargs):
        return redirect('quote_admin')