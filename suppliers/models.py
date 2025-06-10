from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    
    def __str__(self):
        return self.name