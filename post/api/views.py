from accounts.models import User

from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsStaffUser, IsRightUser
from rest_framework import generics, permissions
from post.models import Post, Category
from post.service import PostFilter, PaginationPosts
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
    CategoryDetailSerializer,
    CategoryListSerializer,
)
# you can add django_filter

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


# POST


class CategoryCreateView(generics.CreateAPIView):
    """Adding a category"""
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostCreateView(generics.CreateAPIView):
    """Adding a post"""
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


# GET lists


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )
    filterset_class = PostFilter
    pagination_class = PaginationPosts


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )


# DELETE


class CategoryDestroyView(generics.DestroyAPIView):
    """Deleting category"""
    queryset = Category.objects.all()
    permission_classes = [IsStaffUser]


class PostDestroyView(generics.DestroyAPIView):
    """Deleting post"""
    queryset = Post.objects.all()
    permission_classes = [IsStaffUser]


# class PostListView(generics.ListAPIView):
#     """Returning list of posts"""
#     queryset = Post.objects.all()
#     serializer_class = PostListSerializer
#
#
# class PostDetailView(generics.RetrieveAPIView):
#     """Returning single a post"""
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer


# class CategoryListView(generics.ListAPIView):
#     """Returning list of categories"""
#     queryset = Category.objects.all()
#     serializer_class = CategoryListSerializer
#
#
# class CategoryDetailView(generics.RetrieveAPIView):
#     """Returning a single category"""
#     queryset = Category.objects.all()
#     serializer_class = CategoryDetailSerializer

# class PostListView(APIView):
#     """Returning list of posts"""
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostListSerializer(posts, many=True)
#         return Response(serializer.data)


# class PostDetailView(APIView):
#     """Returning single post"""
#     def get(self, request, pk):
#         post = Post.objects.get(id=pk)
#         serializer = PostDetailSerializer(post)
#         return Response(serializer.data)


# class CommentCreateView(generics.CreateAPIView):
#     """Adding comments to the post"""
#     serializer_class = CommentCreateSerializer
