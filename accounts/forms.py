from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "profile_picture",
            )
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm
        fields = (
            "first_name",
            "last_name",
            "date_of_birth",
            "profile_picture",
            )