from rest_framework import generics

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class ListPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ListComment(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class DetailComment(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
