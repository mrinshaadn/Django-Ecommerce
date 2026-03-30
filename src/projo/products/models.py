from django.db import models
from category.models import Category
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE,
        related_name="products",
        null=True, blank=True
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120, blank=True, null=True)
    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True
    )

    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    is_primary = models.BooleanField(default=False)


class VariationManger(models.Manager):
    def colors(self):
        return super(VariationManger, self).filter(variation_category='color', is_active=True)

    # def sizes(self):
    #     return super(VariationManger, self).filter(variation_category='size', is_active=True)


variation_category_choices = (
    ('color', 'color'),
)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choices)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    objects = VariationManger()

    def __str__(self):
        return self.variation_value
