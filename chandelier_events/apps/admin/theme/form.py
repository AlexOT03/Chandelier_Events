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