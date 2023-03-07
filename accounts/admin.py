from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, FriendRequest

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "first_name",
        "last_name",
        "email",
        "is_superuser",
    ]
    fieldsets = ((None, {"fields": ("email", "first_name", "last_name", "date_of_birth", "profile_picture", "friends",)}),)
    add_fieldsets = ((None, {"fields": ("email", "password1", "password2",)}),)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(FriendRequest)