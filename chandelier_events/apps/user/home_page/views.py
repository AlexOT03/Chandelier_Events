from django.shortcuts import render, redirect
from django.views import View
from chandelier_events.apps.admin.quote.models import Quote
from chandelier_events.apps.admin.quote.form import QuotesForm
from chandelier_events.apps.admin.service.models import Service, ServiceDetail
from chandelier_events.apps.admin.location.models import Location, Image, OpeningHour
from chandelier_events.apps.admin.state.models import State
from chandelier_events.apps.admin.theme.models import Theme

# Create your views here.
class homePageView(View):
    def get(self, request, **kwargs):
        states = State.objects.all()
        locations = Location.objects.all()
        locations_images = {}
        
        for location in locations:
            image = Image.objects.filter(location=location).first()
            
            if image:
                locations_images[location.id] = image.image
                print(image.image)
                location.image = locations_images[location.id]
        
        return render(request, 'index.html', {
            'states': states,
            'locations': locations,
        })
    
class quotePageView(View):
    def get(self, request, size, **kwargs):
        service_ids = [0]
        service_ids.append(size)
        form_quote = QuotesForm()
        form_quote.fields['service_detail'].queryset = ServiceDetail.objects.filter(size__in=service_ids)
        
        return render(request, 'quote_user.html', {
            'form_quote': form_quote,
        })

    def post(self, request, size, **kwargs):
        service_ids = [0]
        service_ids.append(size)
        form_quote = QuotesForm(request.POST, request.FILES)
        form_quote.fields['service_detail'].queryset = ServiceDetail.objects.filter(size__in=service_ids)

        if form_quote.is_valid():
            quote = form_quote.save(commit=False)
            selected_service_details = form_quote.cleaned_data['service_detail']
            total_price = sum(service_detail.price for service_detail in selected_service_details)
            quote.total_service = total_price
            quote.save()
            quote.service_detail.set(selected_service_details)
            
            return redirect('home_user')

        return render(request, 'quote_user.html', {
            'form_quote': form_quote,
        })

class locationPageView(View):
    def get(self, request, id, reference, **kwargs):
        locations = Location.objects.all()
        data_info = None
        locations = None
        locations_images = {}
        if reference != "all":
            if reference == "state":
                data_info = State.objects.get(id=id)
                locations = Location.objects.filter(state=id)
                for location in locations:
                    image = Image.objects.filter(location=location).first()
                    if image:
                        locations_images[location.id] = image.image
                        location.image = locations_images[location.id]
                        
            else:
                data_info = Theme.objects.get(id=id)
                locations = Location.objects.filter(theme=id)
                for location in locations:
                    image = Image.objects.filter(location=location).first()
                    if image:
                        locations_images[location.id] = image.image
                        location.image = locations_images[location.id]
                        
        else:
            locations = Location.objects.all()
            for location in locations:
                    image = Image.objects.filter(location=location).first()
                    
                    if image:
                        locations_images[location.id] = image.image
                        location.image = locations_images[location.id]
                        
        new_reference = reference
            
        return render(request, 'location.html', {
            'locations': locations,
            'data_info': data_info,
            'new_reference': new_reference,
        })
    
    def post(self, request, *args, **kwargs):
        return render(request, '')
    
    def show(self, request, id, **kwargs):
        location = Location.objects.get(id=id)
        images = Image.objects.filter(location=location)
        opening_hours = OpeningHour.objects.filter(location=location)
        
        return render(request, 'location_info.html', {
            'location': location,
            'images': images,
            'opening_hours': opening_hours
        })

class aboutPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about_us.html')