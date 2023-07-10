from django import forms
from .models import QuoteDetail
from django.utils.translation import gettext_lazy as _

class QuoteDetailsForm(forms.ModelForm):
    class Meta:
        model = QuoteDetail
        # fields = "__all__"
        exclude = ['folio', 'quote']
        labels = {
            "name": _("Nombre de empleado"),
            "transport": _("Costo por trasnporte"),
            "iva": _("IVA"),
            "discount": _("Descuento"),
            "message": _("Recomendaciones"),
        }