from django.contrib import admin

# Register your models here.

from .models import risk_type, risk_field

admin.site.register(risk_type)
admin.site.register(risk_field)

