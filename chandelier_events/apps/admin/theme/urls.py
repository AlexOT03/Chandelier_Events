from django.urls import path
from .views import themePageView

urlpatterns = [
    path("tematicas/", themePageView.as_view(), name="theme_admin"),
    path("tematica/<id>/informacion", themePageView().show, name="themeInfo_admin"),
    path("tematica/<id>/editar", themePageView().update, name="themeEdit_admin"),
    path("tematica/<id>/eliminar", themePageView().delete, name="themeDelete_admin"),
]