from rest_framework import viewsets, permissions, generics
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from post.models import Post
from rest_framework.response import Response
from .serializers import UserListDetailCreateSerializer
from accounts.models import User
from post.api.permissions import IsStaffUser
from .permissions import IsRightUser


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserListDetailCreateSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserListDetailCreateSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,  IsRightUser)


class UserDestroyView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsStaffUser,)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserListDetailCreateSerializer
    permission_classes = (permissions.IsAuthenticated, )


class UserListView(generics.ListAPIView):
    serializer_class = UserListDetailCreateSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class AddLikedPostView(APIView):
    """Adding a post to the user"""

    def post(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, pk=pk)

        user.liked_posts.add(post)
        user.save()

        data = [post.id for post in user.liked_posts.all()]
        return Response(data=data)


class RemoveLikedPostView(APIView):
    """Removing a post from the user"""

    def delete(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, pk=pk)
        user.liked_posts.remove(post)

        data = [post.id for post in user.liked_posts.all()]
        return Response(data=data)
