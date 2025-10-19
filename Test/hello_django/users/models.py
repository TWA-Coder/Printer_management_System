from django.db import models

# Create your models here.
# class Users(models.Model):
#     email = models.EmailField(max_length=30)
#     password = models.CharField(max_length=50)

# class Person(models.Model):
#     first_name = models.CharField(max_length=70)
#     last_name = models.CharField(max_length=70)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=70)
    price  = models.FloatField(max_length=100)
    category = models.CharField(max_length=50)

# # Retrieving all books
# Product_lq = Product.objects.all()
# #add new products
# mangos = Product(name='mango', description='fruit', price='500', category='food')
# mangos.save()
# banana = Product(name='banana', description='fruit', price='500', category='food')
# banana.save()
# apple = Product(name='apple', description='fruit', price='500', category='food')
# apple.save()
# # Filtering product by type
# products_by_type = Product.objects.filter(name='banana')
