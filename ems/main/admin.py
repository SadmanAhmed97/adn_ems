from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin', 'department', 'designation', 'adn_id',)
    list_filter = ('admin', 'active', 'department',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'is_employee', 'is_manager', 'is_administrator', 'dob', 'full_name', 'department', 'designation', 'adn_id',
            'alternate_email', 'phone', 'alternate_phone', 'gender', 'join', 'address', 'blood_group',)}),
        ('Permissions', {'fields': ('admin', 'staff', 'active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'is_employee', 'is_manager', 'is_administrator', 'full_name',
                'department', 'designation', 'adn_id',
                'alternate_email', 'phone', 'alternate_phone', 'join', 'dob', 'gender', 'address', 'blood_group',)}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)

