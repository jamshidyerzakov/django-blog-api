from rest_framework import serializers
from accounts.models import User
from post.api.serializers import PostIdSerializer


class UserListDetailCreateSerializer(serializers.ModelSerializer):
    """List of Users"""
    liked_posts = PostIdSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
