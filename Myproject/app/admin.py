from django.contrib import admin
from app.models import product,ProductImages
from django.utils.html import format_html

# Register your models here.


class ProductImageModel(admin.StackedInline):
    model=ProductImages

class ProductModel(admin.ModelAdmin):
    list_display=['id','name','get_discription','get_price','get_discount','get_sale_price','file','thumbnil']
    inlines=[ProductImageModel]

    def get_sale_price(self,obj):
        return((obj.price)-(obj.price*(obj.discount/100)))

    def get_discription(self,obj):
        return format_html(f'<span title="{obj.discription}">{obj.discription[0:15]}..... </span>')

    def get_price(self,obj):
        return '₹ '+str(obj.price)

    def get_discount(self,obj):
        return str(obj.discount) +' %'

    get_sale_price.short_description='Sale Price'
    get_discount.short_description='Discount'
    get_price.short_description='MRP'


admin.site.register(product,ProductModel)