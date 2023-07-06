from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.humanize.templatetags.humanize import intcomma

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    tags = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    image = models.ImageField(upload_to='service_images', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class ServiceDetail(models.Model):
    SIZES = (
        (0, "Personalizado"),
        (1, "Pequeño"),
        (2, "Mediano"),
        (3, "Grande"),
    )
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_details')
    size = models.IntegerField(choices=SIZES)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        formatted_price = intcomma(self.price)
        return f"{self.service.name} - ${formatted_price}"
