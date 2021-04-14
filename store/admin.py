from django.contrib import admin

# Register your models here.
from store.models import Product, Tag, Store, ProductImage

admin.site.register(Tag)
admin.site.register(Store)
admin.site.register(ProductImage)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ()
    list_editable = ()
    search_fields = ()
    inlines = []
