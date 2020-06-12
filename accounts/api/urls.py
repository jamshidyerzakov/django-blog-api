from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.UserListView.as_view()),
    path("user/add_post/<int:pk>/", views.AddLikedPostView.as_view()),
    path("user/delete_post/<int:pk>/", views.RemoveLikedPostView.as_view()),
    path("user/<int:pk>/", views.UserDetailView.as_view()),
    path("user/create/", views.UserCreateView.as_view()),
    path("user/delete/<int:pk>/", views.UserDestroyView.as_view()),
    path("user/update/<int:pk>/", views.UserUpdateView.as_view()),
]
