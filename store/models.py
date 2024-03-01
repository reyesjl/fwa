from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_products_by_category(cls, category_name):
        return cls.objects.filter(category=category_name)

    @classmethod
    def get_products_by_brand(cls, brand_name):
        return cls.objects.filter(brand=brand_name)

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
        return self.images.filter(is_main=True).first()

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
        return self.title

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=50, blank=True, null=True)
    material = models.CharField(max_length=250, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50)
    stock_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.title} - {self.size} ({self.color}, {self.material})"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.product.title}"
