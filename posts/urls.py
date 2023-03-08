from django.urls import path
from .views import ListPost, DetailPost, ListComment, DetailComment
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("<int:pk>/", DetailPost.as_view(), name="comment_detail"),
    path("", ListPost.as_view(), name="comment_list"),
    path("comments/<int:pk>/", DetailComment.as_view(), name="comment_detail"),
    path("comments/", ListComment.as_view(), name="comment_list"),
]