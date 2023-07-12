from django.urls import path, include
from .views import homePageView, locationPageView, aboutPageView, quotePageView

urlpatterns = [
    # URL's Home page
    path("", homePageView.as_view(), name="home_user"),
    # URL's location page
    path("ubicaciones/<str:reference>/<id>/", locationPageView.as_view(), name="location_user"),
    path("ubicacion/<id>/informacion", locationPageView().show, name="locationInfo_user"),
    # URL's about us page
    path("nosotros/", aboutPageView.as_view(), name="about_user"),
    # URL's quote page
    # path("cotizar/ubicacion/<id>/", quotePageView.as_view(), name="quote_user"),
    path("cotizar_evento/<size>/<int:id>/", quotePageView.as_view(), name="quote_card_user"),
    # URL's import from message app
    path("", include("chandelier_events.apps.user.message.urls"))
]