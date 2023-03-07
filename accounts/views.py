from rest_framework import generics

from .models import CustomUser, FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer

class ListUser(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ListFriendRequest(generics.ListAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

class DetailFriendRequest(generics.RetrieveAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
