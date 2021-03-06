from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import EmployerProfile, User, Profile


class MyUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    fieldsets = (
        (('User'), {'fields': ('username', 'phone_number',
                               'email', 'first_name', 'last_name', 'is_verified', 'status')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser')})
    )


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['user', 'state']


class EmployerProfileAdmin(admin.ModelAdmin):
    model = EmployerProfile
    list_display = ['user', 'state']


admin.site.register(User, MyUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(EmployerProfile, EmployerProfileAdmin)
