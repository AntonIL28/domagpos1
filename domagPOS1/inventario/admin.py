from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)