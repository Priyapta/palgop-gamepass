from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=255)
    itemDescription = models.TextField()
    itemPrice = models.DecimalField(max_digits=10, decimal_places=2)
    itemid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)