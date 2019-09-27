from django.db import models
from django.conf import settings 
# Create your models here.
class Listing(models.Model):
    name        = models.CharField(max_length=120)
    price       = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    qtyRoom     = models.CharField(max_length=120)
    photo       = models.CharField(max_length=64)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    @property
    def get_photo(self):
        return "{}".format(self.photo)
