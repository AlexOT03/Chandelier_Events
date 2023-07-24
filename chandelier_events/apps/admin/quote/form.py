from django import forms
from .models import Quote
from django.utils.translation import gettext_lazy as _

# create a ModelForm
class MyTimeInput(forms.widgets.TimeInput):
    input_type = 'time'
class MyDateInput(forms.widgets.DateInput):
    input_type = 'date'
    
class QuotesForm(forms.ModelForm):
    date_of_event = forms.DateField(widget=MyDateInput(), label=_("Dia del evento"))
    start_time = forms.TimeField(widget=MyTimeInput(), label=_("Hora de Inicio"))
    end_time = forms.TimeField(widget=MyTimeInput(), label=_("Hora de Fin"))
    
    class Meta:
        model = Quote
        # fields = "__all__"
        exclude = {"total_service", "location"}
        labels = {
            "name": _("Nombre"),
            "last_name": _("Apellido"),
            "email": _("Correo"),
            "phone": _("Telefono"),
            "people": _("Personas"),
            'service_detail': _("Servicios"),
            "theme": _("Tematica"),
            "budget": _("Presupuesto"),
            "message": _("Comentarios"),
            "quote_by_phone": _("Contactar por Llamada"),
            "quote_by_email": _("Contactar por Correo"),
            "quote_by_sms": _("Contactar por Mensaje"),
            "created_date": _("Fecha de creacion"),
        }