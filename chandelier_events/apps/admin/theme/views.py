from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .form import ThemeForm
from .models import Theme

# Create your views here.
class themePageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        themes = Theme.objects.all().order_by('id')
        form_theme = ThemeForm()
        
        return render(request, 'theme.html', {
            'themes': themes,
            'form_theme': form_theme,
        })

    def post(self, request, *args, **kwargs):
        themes = Theme.objects.all().order_by('id')
        form_theme = ThemeForm(request.POST, request.FILES)
        
        if form_theme.is_valid():
            form_theme.save()
        else:
            return render(request, 'theme.html', {
                'themes': themes,
                'form_theme': form_theme
            })
            
        return redirect('theme_admin')
    
    def show(self, request, id, **kwargs):
        theme = Theme.objects.get(id=id)
        
        return render(request, 'theme_info.html', {
            'theme': theme,
        })
    
    def update(self, request, id, **kwargs):
        theme = Theme.objects.get(id=id)
        
        if request.method == 'POST':
            form_theme = ThemeForm(request.POST, request.FILES, instance=theme)
            
            if form_theme.is_valid():
                form_theme.save()
                return redirect('theme_admin')
        else:
            form_theme = ThemeForm(instance=theme)
            
        return render(request, 'theme_edit.html', {
            'theme': theme,
            'form_theme': form_theme,
        })
    
    def delete(self, request, id, **kwargs):
        theme = Theme.objects.get(id=id)
        theme.delete()
        
        return redirect('theme_admin')