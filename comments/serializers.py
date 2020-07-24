from django.contrib.auth import get_user_model
from rest_framework import serializers

from post.models import Post
from service.general.serializers import RecursiveSerializer
from service.comment.serializers import FilterCommentSerializer

from .models import Comment


User = get_user_model()


class CommentCreateSerializer(serializers.ModelSerializer):
    """Creating comment"""

    class Meta:
        model = Comment
        fields = '__all__'


class CommenterSerializer(serializers.ModelSerializer):
    """Serializing the user as commenter"""

    url = serializers.HyperlinkedIdentityField(view_name="account:user-detail")

    class Meta:
        model = User
        fields = ("id", "email", "url")


class RelatedPostSerializer(serializers.ModelSerializer):
    """Serializing id and url of Post model"""

    class Meta:
        model = Post
        fields = ("id", "url")


class CommentSerializer(serializers.ModelSerializer):
    """Serializing Comment model for list and detail display"""
    commenter = CommenterSerializer(read_only=True)
    children = RecursiveSerializer(many=True)
    post = RelatedPostSerializer(read_only=True)

    class Meta:
        list_serializer_class = FilterCommentSerializer
        model = Comment
        fields = ("commenter", "post", "content", "date_created", "children", "url")
