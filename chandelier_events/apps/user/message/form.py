from django import forms
from .models import Message
from django.utils.translation import gettext_lazy as _

# create a ModelForm
class MessageForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Message
        fields = "__all__"
        labels = {
            "name": _("Nombre"),
            "email": _("Correo"),
            "phone": _("Telefono"),
            "date": _("Fecha"),
            "affair": _("Asunto"),
            "message": _("Mensaje"),
        }