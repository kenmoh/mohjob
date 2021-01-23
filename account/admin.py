from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User, Profile
from .forms import CreateUserForm


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
    list_display = ['user', 'state', 'location']


admin.site.register(User, MyUserAdmin)
admin.site.register(Profile, ProfileAdmin)
