"""user admin classes"""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.db.models.expressions import F

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Regiser your models here
# admin.site.register(Profile)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin
    """
    list_display = ("pk","nickname", "phone_number", "website", "picture")
    list_display_links = ("pk","nickname",)
    list_editable = ("phone_number", "website", "picture")

    search_fields = (
        "user__email",
        "user__nickname",
        "user__firstname",
        "phone_number", 
        "biography", 
        "website"
    )
    list_filter = (
        "created",
        "modified",
        "nickname__is_active",
        "nickname__is_staff", 
    )

    fieldsets = (
        ("Profile",{
            "fields" : (("nickname", "picture"), ("biography", "website"),), 
        }),
        ("Extra info", {
            "fields" : ("phone_number", ("created","modified"),)
        })
    )

    readonly_fields = ("created", "modified")


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users.
    """
    model = Profile
    can_delete = False
    verbose_name = "profiles"


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin """

    inlines = (ProfileInline,)

    list_display = (
        "pk",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff"
    )

# User models unregister
admin.site.unregister(User)
# Register the User and add UserAdmin
admin.site.register(User, UserAdmin)