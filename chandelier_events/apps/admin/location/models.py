from django.db import models
from chandelier_events.apps.admin.state.models import State
from chandelier_events.apps.admin.theme.models import Theme

# Create your models here.
class Location(models.Model):
    SIZES = (
        (1, 'Pequeño'),
        (2, 'Mediano'),
        (3, 'Grande'),
    )
    
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    location_url = models.URLField(blank=True, null=True)
    length = models.CharField(max_length=200, blank=True, null=True)
    width = models.CharField(max_length=200, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    theme = models.ForeignKey(Theme, on_delete=models.PROTECT)
    capacity = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    web_site = models.URLField(blank=True, null=True)
    parking = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    size = models.IntegerField(choices=SIZES)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
      
class Image(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='location_images', blank=True, null=True)

    # def __str__(self):
    #     return str(self.image)

class OpeningHour(models.Model):
    WEEKDAYS = (
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miércoles'),
        (4, 'Jueves'),
        (5, 'Viernes'),
        (6, 'Sábado'),
        (7, 'Domingo'),
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='opening_hours')
    day_of_week = models.IntegerField(choices=WEEKDAYS, blank=True, null=True)
    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)

    # def __str__(self):
    #     return self.day_of_week