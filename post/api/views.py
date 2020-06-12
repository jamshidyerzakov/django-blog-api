from accounts.models import User

from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAdminUser, IsStaffUser, IsRightUser
from rest_framework import generics, permissions
from post.models import Post, Comment, Category
from post.service import PostFilter, PaginationPosts
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
    CommentCreateSerializer,
    CommentSerializer,
    CategoryDetailSerializer,
    CategoryListSerializer,
    CategorySerializer,
)

# GET

class PostDetailView(generics.RetrieveAPIView):
    """Retrieving a post"""
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryDetailView(generics.RetrieveAPIView):
    """Retrieving a category"""
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentDetailView(generics.RetrieveAPIView):
    """Retrieving a comment"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



# PATCH, PUT


class CategoryUpdateView(generics.UpdateAPIView):
    """Updating category"""
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsRightUser]


class PostUpdateView(generics.UpdateAPIView):
    """Updating post"""
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsRightUser]


class CommentUpdateView(generics.UpdateAPIView):
    """Updating comment"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsRightUser]


# POST


class CommentCreateView(generics.CreateAPIView):
    """Adding comments to the post"""
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryCreateView(generics.CreateAPIView):
    """Adding a category"""
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostCreateView(generics.CreateAPIView):
    """Adding a post"""
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


# GET lists


class CommentListView(generics.ListAPIView):
        """Getting list of comments"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )


class PostListView(generics.ListAPIView):
        """Getting list of posts"""
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )
    filterset_class = PostFilter
    pagination_class = PaginationPosts


class CategoryListView(generics.ListAPIView):
        """Getting list of categories"""
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )


# DELETE


class CategoryDestroyView(generics.DestroyAPIView):
    """Deleting category"""
    queryset = Category.objects.all()
    permission_classes = [IsStaffUser]


class CommentDestroyView(generics.DestroyAPIView):
    """Deleting comment"""
    queryset = Comment.objects.all()
    permission_classes = [IsStaffUser]


class PostDestroyView(generics.DestroyAPIView):
    """Deleting post"""
    queryset = Post.objects.all()
    permission_classes = [IsStaffUser]