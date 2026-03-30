from django.db import models
from django.conf import settings
# your product model import adjust
from products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # ← ഇത് മാത്രം മാറ്റിയാൽ മതി
        on_delete=models.CASCADE,
        related_name='wishlist'
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlisted_by')
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # duplicate add ആകില്ല

    def __str__(self):
        return f"{self.user.username} → {self.product.name}"