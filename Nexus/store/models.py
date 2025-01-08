from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, null=True)
    image = models.ImageField(null=True, blank=True)
    price = models.FloatField()

class Cart(models.Model):
    total_price = models.FloatField()

class Order(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    total_price = models.FloatField()
    status = models.CharField(max_length=50)
    
class Cart_item(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

class Order_item(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()