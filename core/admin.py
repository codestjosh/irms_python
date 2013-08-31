from .models import Category, Designer, Product, Customer, Sale, Order
from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'designer', 'colour', 'price', 'quantity', 'on_sales_bool']
    list_filter = ['on_sales_bool', 'price', 'designer']
    search_fields = ['name']

    class Meta:
        pass

admin.site.register(Category)
admin.site.register(Designer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(Order)


