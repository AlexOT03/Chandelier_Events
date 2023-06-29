from django.urls import path
from .views import messagepageView

urlpatterns = [
    path("contactanos/", messagepageView.as_view(), name="message_user")
]