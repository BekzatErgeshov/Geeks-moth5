from django.contrib import admin
from app.settings.models import Category, Product, ProductImage

admin.site.register(Category)
# admin.site.register(ProductImage)
# admin.site.register(Product)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price")
    list_filter = ("name", "category", "price")
    inlines = [ProductImageInline]