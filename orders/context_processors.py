from .models import CartItem
from products.models import Wishlist

def cart_count(request):
    if request.user.is_authenticated:
        return {
            'cart_count': CartItem.objects.filter(user=request.user).count(),
            'wishlist_count': Wishlist.objects.filter(user=request.user).count(),
        }
    return {
        'cart_count': 0,
        'wishlist_count': 0
    }

