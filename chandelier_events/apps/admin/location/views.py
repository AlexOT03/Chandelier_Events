from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.forms import formset_factory
from django.forms.models import modelformset_factory
from .form import LocationsForm, OpeningHoursForm, ImagesForm
from .models import Location, OpeningHour, Image

# Create your views here.
class locationPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all().order_by('id')
        locations_images = {}
        
        for location in locations:
            image = Image.objects.filter(location=location).first()
            
            if image:
                locations_images[location.id] = image.image
                print(image.image)
                location.image = locations_images[location.id]
                
        form_location = LocationsForm()
        
        form_class_hours = formset_factory(OpeningHoursForm, extra=7, max_num=7)
        form_hours = form_class_hours(initial=[
            {'day_of_week': 1},  # Lunes
            {'day_of_week': 2},  # Martes
            {'day_of_week': 3},  # Miércoles
            {'day_of_week': 4},  # Jueves
            {'day_of_week': 5},  # Viernes
            {'day_of_week': 6},  # Sábado
            {'day_of_week': 7},  # Domingo
        ])
        
        form_class_images = formset_factory(ImagesForm, extra=5, max_num=5)
        form_images = form_class_images()
        
        return render(request, 'location_admin.html', {
            'locations': locations,
            'form_location': form_location,
            'form_hours': form_hours,
            'form_images': form_images,
        })
        
    def post(self, request, *args, **kwargs):
        locations = Location.objects.all().order_by('id')
        form_location = LocationsForm(request.POST, request.FILES)

        form_class_hours = formset_factory(OpeningHoursForm, extra=7, max_num=7)
        form_hours = form_class_hours(request.POST)

        form_class_images = formset_factory(ImagesForm, extra=5)
        form_images = form_class_images(request.POST, request.FILES)

        if form_location.is_valid() and form_hours.is_valid() and form_images.is_valid():
            location = form_location.save()

            for form in form_hours:
                hours = form.save(commit=False)
                hours.location = location
                hours.save()
                
            for i, form in enumerate(form_images):
                if i < 5:  # Limitar el número de formularios guardados a 5
                    image = form.save(commit=False)
                    image.location = location
                    image.save()

            # for form in form_images:
            #     image = form.save(commit=False)
            #     image.location = location
            #     image.save()

            return redirect('location_admin')

        else:
            return render(request, 'location_admin.html', {
                'locations': locations,
                'form_location': form_location,
                'form_hours': form_hours,
                'form_images': form_images,
            })
    
    def show(self, request, id, **kwargs):
        location = Location.objects.get(id=id)
        opening_hours = OpeningHour.objects.filter(location=location)
        images = Image.objects.filter(location=location)
        
        return render(request, 'location_admin_info.html', {
            'location': location,
            'opening_hours': opening_hours,
            'images': images
        })
    
    def update(self, request, id, **kwargs):
        location = Location.objects.get(id=id)
        location_opening_hours = OpeningHour.objects.filter(location=location)
        location_images = Image.objects.filter(location=location)
        
        formset_hours = modelformset_factory(OpeningHour, extra=0, form=OpeningHoursForm)
        formset_images = modelformset_factory(Image, extra=0, form=ImagesForm)
        
        if request.method == 'POST':
            form_location = LocationsForm(request.POST, instance=location)
            form_hours = formset_hours(request.POST, queryset=location_opening_hours)
            form_images = formset_images(request.POST, request.FILES, queryset=location_images)
            
            if form_location.is_valid() and form_hours.is_valid() and form_images.is_valid():
                location = form_location.save()
                
                for form in form_hours:
                    hours = form.save(commit=False)
                    hours.location = location
                    hours.save()

                for form in form_images:
                    image = form.save(commit=False)
                    image.location = location
                    image.save()

            return redirect('location_admin')
            
        else:
            form_location = LocationsForm(instance=location)
            form_hours = formset_hours(queryset=location_opening_hours)
            form_images = formset_images(queryset=location_images)
        
        return render(request, 'location_admin_edit.html', {
            'form_location': form_location,
            'form_hours': form_hours,
            'form_images': form_images,
        })
    
    def delete(self, request, id, **kwargs):
        location = Location.objects.get(id=id)
        location.delete()
        
        return redirect('location_admin')