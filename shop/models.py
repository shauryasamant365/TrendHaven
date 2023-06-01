from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('books', 'Books'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    country_of_origin = models.CharField(default='India', max_length=15)
    inventory = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    ratings = models.DecimalField(max_digits=3, decimal_places=2)
    # Additional fields can be added as per your requirements

    def __str__(self):
        return self.title


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100, default='')
    is_verified = models.BooleanField(default=False)


class Testimonial(models.Model):
    title = models.CharField(default="", max_length=50)
    rating = models.IntegerField(default="")
    review = models.CharField(default="", max_length=500)
    name = models.CharField(default="", max_length=50)
    designation = models.CharField(default="", max_length=50)
    image = models.ImageField(default='', upload_to='media/testimonials/images/')
    
    def __str__(self):
        return f"{self.title} ({self.name})"
        

class Cart(models.Model):
    belongs_to = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.belongs_to.first_name.title()} {self.belongs_to.last_name.title()}'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product} ({self.cart.belongs_to.username})"


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('suspended', 'Suspended'),
    ]
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_holder = models.CharField(default="", max_length=100)
    card_number = models.CharField(default="", max_length=100)
    validity = models.CharField(default="", max_length=100)
    cvv = models.CharField(default="", max_length=50)
    street_address = models.CharField(default="", max_length=500)
    state = models.CharField(default="", max_length=50)
    zip = models.IntegerField(default="")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s order ({self.date})"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order #{self.order.id} - {self.product.title}"


class SavedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.product.title} saved by {self.user.first_name}"
