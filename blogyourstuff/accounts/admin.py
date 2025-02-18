from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class UserProfileAdmin(UserAdmin):
    model = UserProfile
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

admin.site.register(UserProfile, UserProfileAdmin)