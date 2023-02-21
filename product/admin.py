from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.OrderStatus)
admin.site.register(models.ProductOrder)
admin.site.register(models.UserOrder)




