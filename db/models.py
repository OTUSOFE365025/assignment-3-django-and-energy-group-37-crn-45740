import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    # UPC-A standard used in North America
    upc = models.CharField(max_length=12)
