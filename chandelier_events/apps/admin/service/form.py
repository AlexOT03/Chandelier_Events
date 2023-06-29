from django import forms
from .models import Service, ServiceDetail
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