from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class adminPageView(View):
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

class messagePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'message_admin.html')
    
    def post(self, request, *args, **kwargs):
        return redirect('message_admin')
    
    def show(self, request, *args, **kwargs):
        return render(request, 'message_admin_info.html')
    
    def update(self, request, *args, **kwargs):
        return redirect('message_admin')
    
    def delete(self, request, *args, **kwargs):
        return redirect('message_admin')