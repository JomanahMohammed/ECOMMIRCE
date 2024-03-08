from django.contrib import admin

from .models import Items,ItemDetails,Device,DeviceDetails
# Register your models here.

admin.site.register(Items)
admin.site.register(ItemDetails)

admin.site.register(Device)
admin.site.register(DeviceDetails)