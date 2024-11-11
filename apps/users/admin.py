# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# Extend the UserAdmin to display additional fields in the admin panel
class CustomUserAdmin(BaseUserAdmin):
    # Specify fields to display in list view
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
        "is_active",
    )

    # Specify fields to filter by
    list_filter = ("is_staff", "is_active", "role")

    # Specify search fields
    search_fields = ("username", "email", "first_name", "last_name")

    # Define fieldsets to customize form layout
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Role", {"fields": ("role",)}),  # Add custom field here
    )

    # Define the fields for the "add user" form
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "role",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


# Register the custom User model with the modified UserAdmin
admin.site.register(User, CustomUserAdmin)
