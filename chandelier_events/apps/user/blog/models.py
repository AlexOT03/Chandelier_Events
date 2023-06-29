from django.db import models

# Create your models here.
class Post(models.Model):
    
    RATING = [
        (1, "1 estrella"),
        (2, "2 estrellas"),
        (3, "3 estrellas"),
        (4, "4 estrellas"),
        (5, "5 estrellas"),
    ]
    
    author = models.CharField(max_length=200)
    stars = models.IntegerField(choices=RATING, blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return self.author