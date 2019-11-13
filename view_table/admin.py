from django.contrib import admin
from .models import Customuser
# Register your models here.

@admin.register(Customuser)
class CustomuserAdmin(admin.ModelAdmin):
    pass
