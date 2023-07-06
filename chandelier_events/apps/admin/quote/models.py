from django.db import models
from chandelier_events.apps.admin.service.models import Service
from chandelier_events.apps.admin.service.models import Service, ServiceDetail
from chandelier_events.apps.admin.location.models import Location

# Create your models here.
class Quote(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True, null=True)
    date_of_event = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    people = models.IntegerField()
    service_detail = models.ManyToManyField(ServiceDetail)
    budget = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    message = models.TextField(blank=True)
    quote_by_phone = models.BooleanField(default=False)
    quote_by_email = models.BooleanField(default=True)
    quote_by_sms = models.BooleanField(default=False)
    total_service = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cotización #{self.pk}'