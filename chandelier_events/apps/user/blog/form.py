from django import forms
from .models import Post
from django.utils.translation import gettext_lazy as _

class PostsForm(forms.Form):
    class Meta:
        model = Post
        fields = "__all__"
        lables = {
            "author": _("Usuario"),
            "stars": _("Estrellas"),
            "title": _("Titulo"),
            "content": _("Contenido"),
            "created_at": _("Fecha"),
        }