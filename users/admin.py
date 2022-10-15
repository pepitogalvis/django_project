from django.contrib import admin
from .models import NewUser
from .models import Doctor
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff','role')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name',
                    'is_active', 'is_staff','role')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff','role','phone','ssn')}
         ),
    )

class DoctorAdminConfig(UserAdmin):
    model = Doctor
    search_fields = ('email', 'ssn')
    list_filter = ('email', 'user_name', 'last_name', 'is_active')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name','last_name',
                    'is_active', 'ssn', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name','last_name')}),
        ('Permissions', {'fields': ('is_active', 'role')}),
        ('Personal', {'fields': ('about','ssn','phone')}),
    )
    formfield_overrides = {
        Doctor.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name','last_name', 'password1', 'password2', 'is_active','phone','role','ssn')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
admin.site.register(Doctor, DoctorAdminConfig)
