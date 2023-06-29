from django.urls import path
from .views import quotePageView

urlpatterns = [
    path("cotizaciones/", quotePageView.as_view(), name="quote_admin"),
    path("cotizacion/<id>/informacion/", quotePageView().show, name="quoteInfo_admin"),
    path("cotizacion/<id>/editar/", quotePageView().update, name="quoteEdit_editar"),
    path("cotizacion/<id>/eliminar/", quotePageView().delete, name="quoteDelete_admin"),
]