from django.contrib import admin

# Register your models here.

from eggfarm.models import Orders,Invoice, Prices, Capacity

admin.site.register(Orders)
admin.site.register(Invoice)
admin.site.register(Prices)
admin.site.register(Capacity)