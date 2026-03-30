from django import template
from wishlist.models import Wishlist  # adjust app name

register = template.Library()


@register.simple_tag
def is_wishlisted(user, product):
    """Returns True if product is in user's wishlist."""
    if not user.is_authenticated:
        return False
    return Wishlist.objects.filter(user=user, product=product).exists()
