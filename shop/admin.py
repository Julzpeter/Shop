from django.contrib import admin
from .models import Category, Product,Order,OrderItem

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created','updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price','stock','available']
    prepopoluated_fields = {'slug': ('name',)}
admin.site.register(Product,ProductAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
