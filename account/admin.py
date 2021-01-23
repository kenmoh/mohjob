from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from .forms import CreateUserForm


class MyUserAdmin(UserAdmin):
    add_form = CreateUserForm


admin.site.register(User, MyUserAdmin)
admin.site.register(Profile)
