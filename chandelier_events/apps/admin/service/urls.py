from django.urls import path
from .views import servicePageView

urlpatterns = [
    path("servicios/", servicePageView.as_view(), name="service_admin"),
    path("servicio/<id>/informacion/", servicePageView().show, name="serviceInfo_admin"),
    path("servicio/<id>/editar/", servicePageView().update, name="serviceEdit_admin"),
    path("servicio/<id>/eliminar/", servicePageView().delete, name="serviceDelete_admin"),
]