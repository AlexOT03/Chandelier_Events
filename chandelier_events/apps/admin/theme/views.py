from django.shortcuts import render, redirect
from django.views import View
from .form import ThemeForm
from .models import Theme

# Create your views here.
class themePageView(View):
    def get(self, request, *args, **kwargs):
        themes = Theme.objects.all()
        form_theme = ThemeForm()
        return render(request, 'theme.html', {
            'themes': themes,
            'form_theme': form_theme,
        })

    def post(self, request, *args, **kwargs):
        return redirect('theme_admin')
    
    def show(self, request, *args, **kwargs):
        return render(request, 'theme_info.html')
    
    def update(self, request, *args, **kwargs):
        return redirect('theme_admin')
    
    def delete(self, request, *args, **kwargs):
        return redirect('theme_admin')