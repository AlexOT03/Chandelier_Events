from django.urls import path
from .views import quotePageView, ViewPDF, DownloadPDF

urlpatterns = [
    path("cotizaciones/", quotePageView.as_view(), name="quote_admin"),
    path("cotizacion/<id>/informacion/", quotePageView().show, name="quoteInfo_admin"),
    path("cotizacion/<id>/eliminar/", quotePageView().delete, name="quoteDelete_admin"),
    
    path("cotizacion/<id>/view_pdf/", ViewPDF.as_view(), name="pdf_view"),
    path("cotizacion/<id>/download_pdf", DownloadPDF.as_view(), name="pdf_download"),
]