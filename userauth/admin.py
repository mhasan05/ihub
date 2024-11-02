from django.contrib import admin
from userauth.models import UserAuth
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


class UserAuthAdmin(UserAdmin):
    search_fields = ('username',)

    list_display = ['first_name','last_name','email', 'phone','date_joined','is_active']
    fieldsets = UserAdmin.fieldsets + (
            ('Account Summary', {'fields': ('profile_pic','phone','sponsor_id','average_rating',)}),
    )

    add_fieldsets = (
            (
                None,
                {
                    'classes': ('wide',),
                    'fields': ('profile_pic','username', 'first_name', 'last_name','email','phone','sponsor_id', 'password1', 'password2'),
                },
            ),
        )
    ordering = ('-date_joined',)
admin.site.register(UserAuth,UserAuthAdmin)
admin.site.unregister(Group)