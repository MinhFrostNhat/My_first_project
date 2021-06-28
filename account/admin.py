from django.contrib import admin
from .models import order
from .models import cart1
# Register your models here.

admin.site.register(order)
admin.site.register(cart1)
admin.site.site_header='ATN'