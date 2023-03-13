from rest_framework import serializers
from django.conf import settings

from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "body",
            "image",
            "author",
            "created_at",
            "likes",
            "liked_by",
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "comment",
            "author",
            "post",
            "created_at",
            "likes",
            "liked_by",
        )