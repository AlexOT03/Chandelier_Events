from django.urls import path, include
from .views import adminPageView, messagePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", adminPageView.as_view(), name="home_admin"),
    
    # Message URL's
    path("admin/mensajes/", messagePageView.as_view(), name="message_admin"),
    path("admin/mensaje/<id>/informacion/", messagePageView().show, name="messageInfo_admin"),
    
    # Quote URL's
    path("admin/", include("chandelier_events.apps.admin.quote.urls")),
    
    # Location URL's
    path("admin/", include("chandelier_events.apps.admin.location.urls")),
    
    # Service URL's
    path("admin/", include("chandelier_events.apps.admin.service.urls")),
    
    # State URL's
    path("admin/", include("chandelier_events.apps.admin.state.urls")),
    
    # Theme URL's
    path("admin/", include("chandelier_events.apps.admin.theme.urls")),
    
    # Login URL
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Reset URL's
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/reset_password.html'), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/reset_password_done.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset_password_complete.html'), name='password_reset_complete'),
]