from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Menu(models.Model):
    ITEM_TYPE = [
        ("B", "Breakfast"),
        ("L", "Lunch"),
        ("D", "Dinner"),
        ("S", "Snack"),
        ("O", "Other"),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="menu_images/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=1, choices=ITEM_TYPE)

    def __str__(self):
        return self.name

# one to many relationship

class ItemReview(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"user {self.user.username} commented on {self.item.name}"
    
# many to many relationship

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    item_varieties = models.ManyToManyField(Menu, related_name="stores")

    def __str__(self):
        return self.name
    
# one to one relationship

class ItemCertificate(models.Model):
    item = models.OneToOneField(Menu, on_delete=models.CASCADE, related_name="certificate")
    certificate = models.CharField(max_length=100)

    def __str__(self):
        return f"certificate for {self.item.name}"
