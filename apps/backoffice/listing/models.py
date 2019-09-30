from django.db import models
from django.conf import settings 
from apps.backoffice.categories.models import Categories
# Create your models here.
class Listing(models.Model):
    name        = models.CharField(max_length=120)
    price       = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    qtyRoom     = models.CharField(max_length=120)
    photo       = models.CharField(max_length=64)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    category    = models.ForeignKey(Categories,
                related_name='listing_categories',
                on_delete=models.CASCADE)
    @property
    def get_photo(self):
        return "{}".format(self.photo)
