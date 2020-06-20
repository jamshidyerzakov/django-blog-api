from rest_framework import generics
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Comment
from .serializers import (
    CommentCreateSerializer,
    CommentSerializer,
)
from post.api.permissions import IsRightUser, IsStaffUser


class CommentDetailView(generics.RetrieveAPIView):
    """Retrieving a comment"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentUpdateView(generics.UpdateAPIView):
    """Updating comment"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsRightUser]


class CommentCreateView(generics.CreateAPIView):
    """Adding comments to the post"""
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )


class CommentDestroyView(generics.DestroyAPIView):
    """Deleting comment"""
    queryset = Comment.objects.all()
    permission_classes = [IsStaffUser]
