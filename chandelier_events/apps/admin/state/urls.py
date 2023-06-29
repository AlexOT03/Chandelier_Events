from django.urls import path
from .views import statePageView

urlpatterns = [
    path("estados/", statePageView.as_view(), name="state_admin"),
    path("estado/<id>/informacion/", statePageView().show, name="stateInfo_admin"),
    path("estado/<id>/editar/", statePageView().update, name="stateEdit_admin"),
    path("estado/<id>/eliminar/", statePageView().delete, name="stateDelete_admin"),
]