from django import forms
from .models import Service, ServiceDetail
from PIL import Image
from django.utils.translation import gettext_lazy as _

# create a ModelForm
class ServicesForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        labels = {
            "name": _("Nombre"),
            "description": _("Descripcion"),
            "price": _("Precio"),
            "duration": _("Duracion"),
            "is_active": _("Activo"),
            "created_date": _("Fecha de registro"),
            "updated_date": _("Fecha de actualizacion"),
            "tags": _("Etiquetas"),
            "image": _("Imagen"),
        }
        
    def clean_images(self):
        image = self.cleaned_data.get('image', False)
    
        if image:
            desired_width = 1280
            desired_height = 720
    
            img = Image.open(image)
            width, height = img.size
    
            if width > desired_width or height > desired_height:
                
                raise forms.ValidationError(
                    f"La imagen debe tener una anchura mínima de {desired_width}px y una altura mínima de {desired_height}px."
                )
    
        return image
        
class ServiceDetailsForm(forms.ModelForm):
    class Meta:
        model = ServiceDetail
        exclude = ['service']
        labels = {
            "service": _("Servicio"),
            "price": _("Precio"),
            "duration": _("Duracion"),
            "size": _("Tamaño"),
        }