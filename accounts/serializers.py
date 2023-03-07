from rest_framework import serializers

from .models import CustomUser, FriendRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "profile_picture",
            "friends",
        )

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = (
            "id",
            "from_user",
            "to_user",
        )