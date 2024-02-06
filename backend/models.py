from django.core.validators import MinValueValidator , MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField("category/")

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="items/")
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0)])
    category =  models.ForeignKey(Category,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  related_query_name="items")

    def __str__(self):
        return self.name


class Comment(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE,related_name="comments")
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="comments")
    text = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(5)]
    )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}:{self.item}"


class Order(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="orders")

class Payment(models.Model):
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name="payment")
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="payments")
    paymentCode = models.CharField(max_length=70)
    amount = models.FloatField(validators=[MinValueValidator(0)])
    paymentDate = models.DateTimeField(auto_now_add=True)



class OrderItem(models.Model):
    item = models.ForeignKey(Item,on_delete=models.SET_NULL)
    quantity = models.PositiveSmallIntegerField()
    order =  models.ForeignKey(Order,related_name="orderItems",on_delete=models.CASCADE)




