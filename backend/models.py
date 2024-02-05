from django.core.validators import MinValueValidator , MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model

class Item(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0)])



class Comment(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE,related_name="comments")
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="comments")
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])