from rest_framework import serializers

from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "body",
            "image",
            "author",
            "likes",
            "created_at",
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "comment",
            "author",
            "post",
            "likes",
            "created_at",
        )