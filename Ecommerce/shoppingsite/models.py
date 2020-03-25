from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Enter name for a category.')
    description = models.TextField(max_length=1000, help_text='Enter category description', default='')
    image = models.CharField(max_length=500, help_text='Put category image here.')


class Product(models.Model):
    name = models.CharField(max_length=200, help_text='Enter name for a product.')
    price = models.IntegerField(default=0, blank=False)
    sku = models.IntegerField(default=0,blank=False)    # So luong hang trong kho
    description = models.TextField(max_length=1000, help_text='Enter product description', default='')
    image = models.CharField(max_length=500, help_text='Put product image here.')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)


class Customer(AbstractUser):
    address = models.CharField(max_length=500, help_text='Input your address.')
    country = models.CharField(max_length=500, help_text='Input your country.')
    phone = models.CharField(max_length=50, help_text='Enter your number', blank=False)


class Comment(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    title = models.CharField(default='No title', max_length=500)
    rating = models.IntegerField(blank=True, null=True)
    content = models.TextField(default='', max_length=1000)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ammount = models.IntegerField(default = 0)      # Tong so tien
    shipping_address = models.CharField(max_length=500, help_text='Input address.')
    order_date = models.DateTimeField(auto_now_add=True)

    STATUS = (
        ('a', 'accept'),
        ('p', 'pending'),
        ('d', 'decline'),
    )

    order_status = models.CharField(
        choices=STATUS,
        max_length=1,
        default='p',
        help_text='Order status',
        blank=True
    )


class OrderDetail(models.Model):    # Chi tiet 1 item trong gio hang
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    sku = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

