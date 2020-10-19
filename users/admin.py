from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'username', 'first_name',)
    list_filter = ('email', 'username', 'first_name', 'user_choice', 'user_phone', 'zip_code', 'user_address')
    ordering = ('-start_date',)
    #장고 어드민에서 보여지는 화면
    list_display = ('email', 'username', 'first_name', 'user_choice', 'user_phone', 'zip_code', 'user_address', 'shop',)
    #admin/users/선택후 변경이 가능한 화면
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name','user_choice', 'user_phone', 'zip_code', 'user_address', 'shop',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2','user_choice', 'user_phone', 'zip_code', 'user_address', 'shop',)}
         ),
    )


admin.site.register(User, UserAdminConfig)
