from django.urls import path, include
from .views import quotePageView

urlpatterns = [
    path("cotizaciones/", quotePageView.as_view(), name="quote_admin"),
    path("cotizacion/<id>/informacion/", quotePageView().show, name="quoteInfo_admin"),
    path("cotizacion/<id>/eliminar/", quotePageView().delete, name="quoteDelete_admin"),
    
    path("", include("chandelier_events.apps.admin.quote_pdf.urls")),
]