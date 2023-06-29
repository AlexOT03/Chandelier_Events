from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="state_images")
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name