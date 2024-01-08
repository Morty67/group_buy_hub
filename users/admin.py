from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext as _

from .models import User


class CustomUserAdmin(DjangoUserAdmin):
    """Custom admin model for User model with 'username' field."""

    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
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
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
    )
    search_fields = ("email", "username", "first_name", "last_name")
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
