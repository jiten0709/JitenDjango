from django.db import models
from django.utils import timezone

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
