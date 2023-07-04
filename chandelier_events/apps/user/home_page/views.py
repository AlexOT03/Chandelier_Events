from django.shortcuts import render, redirect
from django.views import View
from chandelier_events.apps.admin.quote.models import Quote
from chandelier_events.apps.admin.quote.form import QuotesForm
from chandelier_events.apps.admin.location.models import Location, Image, OpeningHour
from chandelier_events.apps.admin.state.models import State
from chandelier_events.apps.admin.theme.models import Theme

# Create your views here.
class homePageView(View):
    def get(self, request, *args, **kwargs):
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
    
    def post(self, request, *args, **kwargs):
        return render(request, '')
    
    def show(self, request, *args, **kwargs):
        return render(request, '')
    
    def update(self, request, *args, **kwargs):
        return render(request, '')
    
    def delete(self, request, *args, **kwargs):
        return render(request, '')
    
class quotePageView(View):
    def get(self, request, id, **kwargs):
        form_quote = QuotesForm()
        return render(request, 'quote_user.html', {
            'form_quote': form_quote,
        })
    
    def post(self, request, id, **kwargs):
        location = Location.objects.get(id=id)
        form_quote = QuotesForm(request.POST, request.FILES)
        
        if form_quote.is_valid():
            quote = form_quote.save(commit=False)
            quote.location = location
            quote.save()
            
        else:
            form_quote = QuotesForm(request.POST, request.FILES)
            
            return render(request, 'quote_user.html', {
                'form_quote': form_quote,
            })
        
        return redirect('home_user')
    
    def show(self, request, *args, **kwargs):
        return render(request, '')
    
    def update(self, request, *args, **kwargs):
        return render(request, '')
    
    def delete(self, request, *args, **kwargs):
        return render(request, '')

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
    
    def update(self, request, *args, **kwargs):
        return render(request, '')
    
    def delete(self, request, *args, **kwargs):
        return render(request, '')

class aboutPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about_us.html')
    
    def post(self, request, *args, **kwargs):
        return render(request, '')
    
    def show(self, request, *args, **kwargs):
        return render(request, '')
    
    def update(self, request, *args, **kwargs):
        return render(request, '')
    
    def delete(self, request, *args, **kwargs):
        return render(request, '')