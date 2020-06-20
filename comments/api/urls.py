from django.urls import path
from . import views


urlpatterns = [
    path('comment/', views.CommentListView.as_view()),  # GET list
    path('comment/<int:pk>/', views.CommentDetailView.as_view()),  # GET
    path('comment/update/<int:pk>/', views.CommentUpdateView.as_view()),  # PUT PATCH
    path('comment/delete/<int:pk>/', views.CommentDestroyView.as_view()),  # DELETE
    path('comment/create/', views.CommentCreateView.as_view()),  # POST
]