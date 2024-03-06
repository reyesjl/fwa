from django.utils import timezone
from django.db import models
from django.db.models import Subquery, OuterRef

class ProductManager(models.Manager):
    """
    Custom manager for the Product model.
    Provides additional queryset methods and optimizations.
    """

    def get_queryset(self):
        """
        Return a queryset that filters only available products.
        """
        return super().get_queryset().filter(is_available=True)
    
    def get_products_by_category(self, category_name):
        """
        Return a queryset of products filtered by category name.
        """
        return self.get_queryset().filter(category=category_name)
    
    def get_products_by_brand(self, brand_name):
        """
        Return a queryset of products filtered by brand name.
        """
        return self.get_queryset().filter(brand=brand_name)

class Product(models.Model):
    """
    Model representing a product.
    """

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager() # custom product manager

    def get_main_variant(self):
        """
        Get available variants for the product.
        """
        return self.variants.filter(stock_quantity__gt=0).first()

    def get_available_variants(self):
        """
        Get available variants for the product.
        """
        return self.variants.filter(stock_quantity__gt=0)

    def is_team_item(self):
        """
        Check if the product belongs to the 'Team' category.
        """
        return self.category == 'Team'

    def get_main_image(self):
        """
        Get the main image for the product.
        """
        return self.images.filter(is_main=True).first().image.url

    def is_in_stock(self):
        """
        Check if the product is in stock.
        """
        return self.variants.filter(stock_quantity__gt=0).exists()

    def get_available_sizes(self):
        """
        Get available sizes for the product.
        """
        return self.variants.filter(stock_quantity__gt=0).values_list('size', flat=True).distinct()

    def get_available_colors(self):
        """
        Get available colors for the product.
        """
        return self.variants.filter(stock_quantity__gt=0).values_list('color', flat=True).distinct()

    def __str__(self):
        """
        Return the title of the product.
        """
        return self.title

class ProductVariant(models.Model):
    """
    Model representing a product variant.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=50, blank=True, null=True)
    material = models.CharField(max_length=250, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50)
    stock_quantity = models.IntegerField()

    def __str__(self):
        """
        Return a string representation of the product variant.
        """
        return f"{self.product.title} - {self.size} ({self.color}, {self.material})"

class ProductImage(models.Model):
    """
    Model representing a product image.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        """
        Return a string representation of the product image.
        """
        return f"Image for {self.product.title}"
