from django.urls import path
from .views import locationPageView

urlpatterns = [
    path("ubicaciones/", locationPageView.as_view(), name="location_admin"),
    path("ubicacion/<id>/informacion", locationPageView().show, name="locationInfo_admin"),
    path("ubicacion/<id>/editar", locationPageView().update, name="locationEdit_admin"),
    path("ubicacion/<id>/eliminar", locationPageView().delete, name="locationDelete_admin"),
]