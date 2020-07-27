
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])

    class Cart(models.Model):
        cart_id  = models.CharField(max_length=250, blank= True)
        date_added =models.DateField(auto_now_add = True)
        
        
        class Meta:
            db_table = 'Cart'
            ordering = ['date_added']
            
        def __str__(self):
            return self.cart_id
        
        
    class CartItem(models.Model):
        product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
        cart = models.ForeignKey('shop.Cart', on_delete=models.CASCADE)
        quantity = models.IntegerField()
        active = models.BooleanField(default=True)
        
        
        class Meta:
            db_table = 'CartItem'
            
        def sub_total(self):
            return self.product.price * self.quantity
        
        def __str__(self):
            return self.product