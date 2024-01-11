from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()

    def primary_image_url(self):
        # Assuming a Product has many ProductImages and the first one is the primary
        primary_image = self.productimage_set.first()
        if primary_image and primary_image.image:
            return primary_image.image.url
        return ''
    
    def get_absolute_url(self):
        # Reverse function is used to generate the URL based on the product's primary key
        return reverse('product:product_detail', args=[str(self.pk)])

    def __str__(self):
        return self.name
    
class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    materials = models.CharField(max_length=250)
    weight = models.CharField(max_length=100)
    unique_features = models.TextField()

    def __str__(self):
        return f"Details for {self.product.name}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    caption = models.CharField(blank=True, null=True, max_length=200) 

    def __str__(self):
        return f"Image for {self.product.name}"