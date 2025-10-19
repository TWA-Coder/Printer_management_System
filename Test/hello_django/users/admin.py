from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description','price')
    search_fields = ('name', 'category')
admin.site.register(Product)

# Register your models here.
