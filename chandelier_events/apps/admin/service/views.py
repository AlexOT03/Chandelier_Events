from django.shortcuts import render, redirect
from django.views import View
from django.forms import formset_factory
from django.forms.models import modelformset_factory
from .form import ServicesForm, ServiceDetailsForm
from .models import Service, ServiceDetail

# Create your views here.
class servicePageView(View):
    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        form_service = ServicesForm()
        
        form_service_class = formset_factory(ServiceDetailsForm, extra=0, min_num=3, validate_min=True)
        form_service_details = form_service_class(initial=[
            {'size': 1},  # Chico
            {'size': 2},  # Mediano
            {'size': 3},  # Grande
        ])
        
        return render(request, 'service.html', {
            'services': services,
            'form_service': form_service,
            'form_service_details': form_service_details,
        })
    
    def post(self, request, *args, **kwargs):
        return redirect('service_admin')
    
    def show(self, request, *args, **kwargs):
        return render(request, 'service_info.html')
    
    def update(self, request, *args, **kwargs):
        return redirect('service_admin')
    
    def delete(self, request, *args, **kwargs):
        return redirect('service_admin')