from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Comment, Review, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'role',
        'is_staff',
        'is_superuser',
        'is_active'
    )
    search_fields = (
        'username',
        'first_name',
        'last_name',
        'email'
    )
    list_filter = (
        'role',
        'is_active',
        'is_staff'
    )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions',
         {'fields': ('role', 'is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2',
                       'role', 'is_staff', 'is_active')
        }),
    )
    ordering = ('username',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
