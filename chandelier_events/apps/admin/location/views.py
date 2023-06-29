from django.shortcuts import render, redirect
from django.views import View
from django.forms import formset_factory
from django.forms.models import modelformset_factory
from .form import LocationsForm, OpeningHoursForm, ImagesForm
from .models import Location, OpeningHour, Image

# Create your views here.
class locationPageView(View):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()
        form_location = LocationsForm()
        
        form_class_hours = formset_factory(OpeningHoursForm, extra=0, min_num=7, validate_min=True)
        form_hours = form_class_hours(initial=[
            {'day_of_week': 1},  # Lunes
            {'day_of_week': 2},  # Martes
            {'day_of_week': 3},  # Miércoles
            {'day_of_week': 4},  # Jueves
            {'day_of_week': 5},  # Viernes
            {'day_of_week': 6},  # Sábado
            {'day_of_week': 7},  # Domingo
        ])
        
        form_images = formset_factory(ImagesForm)
        
        return render(request, 'location_admin.html', {
            'locations': locations,
            'form_location': form_location,
            'form_hours': form_hours,
            'form_images': form_images,
        })
    
    def post(self, request, *args, **kwargs):
        return redirect('location_admin')
    
    def show(self, request, *args, **kwargs):
        return render(request, '')
    
    def update(self, request, *args, **kwargs):
        return render(request, '')
    
    def delete(self, request, *args, **kwargs):
        return render(request, '')