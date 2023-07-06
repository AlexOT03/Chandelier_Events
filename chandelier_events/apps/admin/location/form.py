from django import forms
from .models import Location, OpeningHour, Image
# from PIL import Image
from django.utils.translation import gettext_lazy as _

# create a ModelForm
class LocationsForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"
        labels = {
            "name": _("Nombre"),
            "owner": _("Dueño"),
            "location": _("Ubicacion"),
            "location_url": _("Mapa"),
            "length": _("Largo"),
            "width": _("Ancho"),
            "state": _("Estado"),
            "theme": _("Tematica"),
            "capacity": _("Cupo"),
            "email": _("Correo"),
            "phone": _("Telefono"),
            "created_`date": _("Fecha de registro"),
            "updated_date": _("Fecha de actualizacion"),
            "price": _("Precio"),
            "description": _("Descripción"),
            "web_site": _("Sitio web"),
            "is_active": _("Activo"),
            "parking": _("Estacionamiento"),
        }

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['location']
        labels = {
            'location': _('Ubicacion'),
            'image': _('Imagen'),
        }
        
    # def clean_images(self):
    #     image = self.cleaned_data.get('image', False)
    
    #     if image:
    #         desired_width = 1920
    #         desired_height = 1080
    
    #         img = Image.open(image)
    #         width, height = img.size
    
    #         if width > desired_width or height > desired_height:
                
    #             raise forms.ValidationError(
    #                 f"La imagen debe tener una anchura mínima de {desired_width}px y una altura mínima de {desired_height}px."
    #             )
    
    #     return image

class MyTimeInput(forms.widgets.TimeInput):
    input_type = 'time'
        
class OpeningHoursForm(forms.ModelForm):
    opening_time = forms.TimeField(widget=MyTimeInput())
    closing_time = forms.TimeField(widget=MyTimeInput())
    
    class Meta:
        model = OpeningHour
        exclude = {'location'}
        labels = {
            "location": _("Ubicacion"),
            "day_of_week": _("Dia"),
            "opening_time": _("Apertura"),
            "closing_time": _("Cierre"),
        }