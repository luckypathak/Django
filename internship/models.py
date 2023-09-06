from django.db import models

class Category(models.Model):
    categoryname = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryname

class Product(models.Model):
    categoryname = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.product_name
