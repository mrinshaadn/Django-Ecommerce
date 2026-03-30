from django.contrib import admin
from .models import Brand, Product, ProductImage, Variation


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "is_available")
    list_filter = ("is_available",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name", "brand", "category",
        "price", "offer_price",
        "stock", "is_active", "created_at"
    )
    list_filter = ("brand", "category", "is_active")
    prepopulated_fields = {"slug": ("name",)}

    search_fields = ("name", "brand__name")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    inlines = [ProductImageInline]

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')



admin.site.register(Variation, VariationAdmin)
