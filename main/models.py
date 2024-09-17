from django.db import models
import uuid

class Product(models.Model):
    itemName = models.CharField(max_length=255)
    itemDescription = models.TextField()
    itemPrice = models.DecimalField(max_digits=10, decimal_places=2)
    itemid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)