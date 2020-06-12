from django.urls import path
from . import views

urlpatterns = [
    # POST
    path('post/create/', views.PostCreateView.as_view()),
    path('category/create/', views.CategoryCreateView.as_view()),
    path('comment/create/', views.CommentCreateView.as_view()),
    # GET list
    path('post/', views.PostListView.as_view()),
    path('category/', views.CategoryListView.as_view()),
    path('comment/', views.CommentListView.as_view()),
    # GET detail
    path('post/<int:pk>/', views.PostDetailView.as_view()),
    path('category/<int:pk>/', views.CategoryDetailView.as_view()),
    path('comment/<int:pk>/', views.CommentDetailView.as_view()),
    # DELETE
    path('post/delete/<int:pk>/', views.PostDestroyView.as_view()),
    path('category/delete/<int:pk>/', views.CategoryDestroyView.as_view()),
    path('comment/delete/<int:pk>/', views.CommentDestroyView.as_view()),
    # PUT PATCH
    path('post/update/<int:pk>/', views.PostUpdateView.as_view()),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view()),
    path('comment/update/<int:pk>/', views.CommentUpdateView.as_view()),
]