from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.site_title='Event Management System'
admin.site.site_header='Welcome Our Website !'
admin.site.index_title='Event Management System'
    
    
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
      fieldsets = (
        (None, {"fields": ("email", "password",)}),
        (("Personal info"), {"fields": ("first_name", "last_name", "username","phone_number","address",)}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        
    )