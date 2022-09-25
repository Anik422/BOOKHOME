from django.contrib import admin
from cartpage.models import cartlist, items, ShippingAddress
# Register your models here.
admin.site.register(cartlist)
admin.site.register(items)
admin.site.register(ShippingAddress)
