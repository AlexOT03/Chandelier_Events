from django.urls import path, include
from .views import homePageView, locationPageView, aboutPageView

urlpatterns = [
    path("", homePageView.as_view(), name="home_user"),
    
    path("ubicaciones/", locationPageView.as_view(), name="location_user"),
    path("ubicacion/<id>/informacion", locationPageView().show, name="locationInfo_user"),
    
    path("nosotros/", aboutPageView.as_view(), name="about_user"),
    
    # URL's import from message app
    path("", include("chandelier_events.apps.user.message.urls"))
]