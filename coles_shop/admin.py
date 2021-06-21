from django.contrib import admin

# Register your models here.
from coles_shop.models import Product, Category, Review

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
