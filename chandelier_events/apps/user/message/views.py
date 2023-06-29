from django.shortcuts import render
from django.views import View
from .form import MessageForm

# Create your views here.
class messagepageView(View):
    def get(self, request, *args, **kwargs):
        form_message = MessageForm()
        return render(request, 'message.html', {
            'form_message': form_message,
        })
    
    def post(self, request, *args, **kwargs):
        return render(request, '')
    
    def show(self, request, *args, **kwargs):
        return render(request, '')
    
    def update(self, request, *args, **kwargs):
        return render(request, '')
    
    def delete(self, request, *args, **kwargs):
        return render(request, '')