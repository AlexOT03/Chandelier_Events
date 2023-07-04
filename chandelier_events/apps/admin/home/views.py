from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views import View
from chandelier_events.apps.user.message.models import Message

# Create your views here.
class adminPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index_admin.html')
    
    def post(self, request, *args, **kwargs):
        return redirect('message_admin')
    
    def show(self, request, *args, **kwargs):
        return render(request, '')
    
    def update(self, request, *args, **kwargs):
        return redirect('message_admin')
    
    def delete(self, request, *args, **kwargs):
        return redirect('message_admin')

    def logout(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')

class messagePageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'message_admin.html')
    
    def post(self, request, *args, **kwargs):
        return redirect('message_admin')
    
    def show(self, request, id, **kwargs):
        message = Message.objects.get(id=id)
        return render(request, 'message_admin_info.html', {
            'message': message,
        })
    
    def update(self, request, *args, **kwargs):
        return redirect('message_admin')
    
    def delete(self, request, *args, **kwargs):
        return redirect('message_admin')