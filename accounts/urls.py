from django.urls import path
from .views import ListUser, DetailUser, ListFriendRequest, DetailFriendRequest

urlpatterns = [
    path("<int:pk>/", DetailUser.as_view(), name="user_detail"),
    path("", ListUser.as_view(), name="user_list"),
    path("friend_requests/<int:pk>/", DetailFriendRequest.as_view(), name="friend_request_detail"),
    path("friend_requests/", ListFriendRequest.as_view(), name="friend_request_list"),
]