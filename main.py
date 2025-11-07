############################################################################
# Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import Product

############################################################################
# START OF APPLICATION
############################################################################
""" Replace the code below with your own """
if len(sys.argv) < 2:
    print("Missing UPC to scan!")
    sys.exit(1)

upc_lu=sys.argv[1]

Product.objects.all().delete()
Product.objects.create(name="ProductA", price=49.99, upc="200001149995")
Product.objects.create(name="ProductB", price=11.25, upc="200002111254")
Product.objects.create(name="ProductC", price=239.21, upc="200003000454")

# Attempt to find provided item via UPC
try:
    p = Product.objects.get(upc=upc_lu)
    print(f"UPC: {p.upc}, Name: {p.name}, Price: {p.price}")
except Product.DoesNotExist:
    print(f"Product with UPC '{upc_lu}' not found!")
    sys.exit()
