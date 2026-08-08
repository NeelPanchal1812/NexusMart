from django.db import models, connection
from django.conf import settings
from django.contrib.postgres.search import SearchVectorField, SearchVector
from django.contrib.postgres.indexes import GinIndex
from django.core.validators import MinValueValidator, MaxValueValidator


# ================= CATEGORY =================

class Category(models.Model):

    name = models.CharField(max_length=200)

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


# ================= PRODUCT =================

class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)

    # 🔥 Popular product counter
    views = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE
    )

    specifications = models.JSONField(blank=True, null=True)

    image = models.ImageField(upload_to="products/", blank=True, null=True)
    # 🌐 Professional external image (CDN / URL based)
    image_url = models.URLField(blank=True, null=True)

    # PostgreSQL full-text search
    search_vector = SearchVectorField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if connection.vendor == 'postgresql':
            Product.objects.filter(id=self.id).update(
                search_vector=(
                    SearchVector("name", weight="A") +
                    SearchVector("description", weight="B")
                )
            )

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            GinIndex(fields=["search_vector"]),
        ]


# ================= RECENTLY VIEWED =================

class RecentlyViewed(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="recent_views",
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        related_name="recently_viewed",
        on_delete=models.CASCADE
    )

    viewed_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-viewed_at"]

    def __str__(self):
        return f"{self.user} viewed {self.product}"


# ================= PRODUCT GALLERY =================

class ProductImage(models.Model):

    product = models.ForeignKey(
        Product,
        related_name="images",
        on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to="products/gallery/")

    def __str__(self):
        return f"Image for {self.product.name}"


# ================= WISHLIST =================

class Wishlist(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="wishlist_items",
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        related_name="wishlisted_by",
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user} ❤️ {self.product.name}"


# ================= REVIEWS & RATINGS =================

class Review(models.Model):

    product = models.ForeignKey(
        Product,
        related_name="reviews",
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("product", "user")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.product.name} - {self.rating}⭐"
