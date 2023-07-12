from django.urls import path
from .views import ViewPDF, DownloadPDF, QuoteDetailView

urlpatterns = [
        path("cotizacion/<id>/cotizar/", QuoteDetailView.as_view(), name="quoteDetails_admin"),
        path("cotizacion/<id>/actualizar_cotizacion/", QuoteDetailView().update, name="quoteDetailsEdit_admin"),
        # quote in pdf
        path("cotizacion/<id>/view_pdf/", ViewPDF.as_view(), name="pdf_view"),
        path("cotizacion/<id>/download_pdf", DownloadPDF.as_view(), name="pdf_download"),
]