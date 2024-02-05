from django.db import models
from django.core.validators import MinValueValidator

class Item(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0)])


