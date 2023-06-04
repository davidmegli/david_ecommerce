from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug'] # display the name and the slug of the category
    prepopulated_fields = {'slug': ('name',)} # automatically populate the slug field with the name field

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock'] # allows to edit the price and the in_stock fields directly from the list display
    prepopulated_fields = {'slug': ('title',)} # automatically populate the slug field with the title field