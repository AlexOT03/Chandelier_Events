from django import forms
from .models import Theme
from PIL import Image
from django.utils.translation import gettext_lazy as _

# create a ModelForm
class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = "__all__"
        labels = {
            "name": _("Nombre"),
            "description" :_("Descripcion"),
            "image": _("Imagen"),
            "created_date": _("Fecha de registro"),
            "is_active": _("Activo"),
        }
        
    def clean_images(self):
       images = self.cleaned_data.get('images', False)
    
       if images:
           desired_width = 1000
           desired_height = 1000

           img = Image.open(images)
    
           width, height = img.size
    
           if width > desired_width or height > desired_height:
               raise forms.ValidationError(
                   f"La imagen debe tener una anchura mínima de {desired_width}px y una altura mínima de {desired_height}px."
               )
    
       return images