from django.db import models
from chandelier_events.apps.admin.quote.models import Quote
from decimal import Decimal
import uuid

# Create your models here.
class QuoteDetail(models.Model):
    IVA = (
        (Decimal('0.0'), '0'),
        (Decimal('0.05'), '5'),
        (Decimal('0.10'), '10'),
        (Decimal('0.15'), '15'),
    )
    
    folio = models.CharField(max_length=36, default=uuid.uuid4)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    name = models.CharField(max_length=255)
    transport = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True, default=0.00)
    iva = models.DecimalField(choices=IVA, decimal_places=2, max_digits=8)
    discount = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True, default=0.00)
    message = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.quote} - {self.name}"