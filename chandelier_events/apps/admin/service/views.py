from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.forms import formset_factory
from django.forms.models import modelformset_factory
from .form import ServicesForm, ServiceDetailsForm
from .models import Service, ServiceDetail

# Create your views here.
class servicePageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        services = Service.objects.all().order_by('id')
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
        services = Service.objects.all().order_by('id')
        form_service = ServicesForm(request.POST, request.FILES)
        
        form_service_class = formset_factory(ServiceDetailsForm, extra=3)
        form_service_details = form_service_class(request.POST)
        
        if form_service.is_valid() and form_service_details.is_valid():
            service = form_service.save()
            
            for i, form in enumerate(form_service_details):
                if i == 0 and form.cleaned_data['size'] == 0:
                    hours = form.save(commit=False)
                    hours.service = service
                    hours.save()
                    break  # Salir del bucle después de guardar el primer formulario
                else:
                    hours = form.save(commit=False)
                    hours.service = service
                    hours.save()
            
            # for i, form in enumerate(form_service_details):
            #     if i == 0 and form.cleaned_data['size'] == 0:
            #         hours = form.save(commit=False)
            #         hours.service = service
            #         hours.save()
            #         break  # Exit the loop after saving the first form
            #     else:
            #         hours = form.save(commit=False)
            #         hours.service = service
            #         hours.save()
            
            # for i, form in enumerate(form_service_details):
            #     if i == 0 or form.cleaned_data['size'] != 0:
            #         hours = form.save(commit=False)
            #         hours.service = service
            #         hours.save()
            
            # for form in form_service_details:
            #        hours = form.save(commit=False)
            #        hours.service = service
            #        hours.save()
            
        else:
            return render(request, 'service.html', {
            'services': services,
            'form_service': form_service,
            'form_service_details': form_service_details,
        })
        
        return redirect('service_admin')
    
    def show(self, request, id, **kwargs):
        service = Service.objects.get(id=id)
        service_details = ServiceDetail.objects.filter(service=service)
        
        return render(request, 'service_info.html', {
            'service': service,
            'service_details': service_details,
        })
    
    def update(self, request, id, **kwargs):
        service = Service.objects.get(id=id)
        service_details = ServiceDetail.objects.filter(service=service)
        
        formset = modelformset_factory(ServiceDetail, extra=0, form=ServiceDetailsForm)
        
        if request.method == 'POST':
            form_service = ServicesForm(request.POST, request.FILES, instance=service)
            form_service_details = formset(request.POST, request.FILES, queryset=service_details)
            
            if form_service.is_valid() and form_service_details.is_valid():
                service = form_service.save()
                
                for form in form_service_details:
                    service_detail = form.save(commit=False)
                    service_detail.service = service
                    service_detail.save()
                    
                return redirect('service_admin')
            
        else:
            form_service = ServicesForm(instance=service)
            form_service_details = formset(queryset=service_details)
        
        return render(request, 'service_edit.html', {
            'service': service,
            'form_service': form_service,
            'form_service_details': form_service_details
        })
    
    def delete(self, request, id, **kwargs):
        service = Service.objects.get(id=id)
        service.delete()
        
        return redirect('service_admin')