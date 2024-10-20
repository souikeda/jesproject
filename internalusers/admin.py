from django.contrib import admin
from .models import User, JesUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user_type', 'is_active', 'is_staff')
    list_filter = ('user_type', 'is_active', 'is_staff')
    search_fields = ('name', 'email')
    ordering = ('name',)

class JesUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'department')
    search_fields = ('user__name', 'department')

admin.site.register(User, UserAdmin)
admin.site.register(JesUser, JesUserAdmin)
