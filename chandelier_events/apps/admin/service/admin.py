from django.contrib import admin
from .models import Service, ServiceDetail

# Register your models here.
admin.site.register(Service)
admin.site.register(ServiceDetail)