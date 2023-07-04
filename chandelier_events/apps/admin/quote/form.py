from django import forms
from .models import Quote
from django.utils.translation import gettext_lazy as _

# create a ModelForm
class QuotesForm(forms.ModelForm):
    class Meta:
        model = Quote
        # fields = "__all__"
        exclude = {"location"}
        labels = {
            "name": _("Nombres"),
            "last_name": _("Apellidos"),
            "email": _("Correo"),
            "phone": _("Telefono"),
            "date_fo_event": _("Dia del evento"),
            "start_time": _("Hora de Inicio"),
            "end_time": _("Hora de Fin"),
            "people": _("Personas"),
            "service": _("Servicio"),
            # "location": _("Ubicacion"),
            "budget": _("Presupuesto"),
            "quote_by_phone": _("Contactar por Llamada"),
            "quote_by_email": _("Contactar por Correo"),
            "quote_by_sms": _("Contactar por Mensaje"),
            "created_date": _("Fecha de creacion"),
        }