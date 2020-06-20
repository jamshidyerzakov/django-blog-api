
from rest_framework import serializers
from ..models import Comment
from accounts.models import User
from post.service import RecursiveSerializer


class FilterCommentSerializer(serializers.ListSerializer):
    """Filtering comments, only parents"""
    def to_representation(self, data):
        data = data.filter(reply_to=None)
        return super().to_representation(data)


class CommentCreateSerializer(serializers.ModelSerializer):
    """Creating comment"""

    class Meta:
        model = Comment
        fields = '__all__'


class CommenterSerializer(serializers.ModelSerializer):
    """Commenter"""

    class Meta:
        model = User
        fields = ("email", "img")


class CommentSerializer(serializers.ModelSerializer):
    """Displaying comments"""
    commenter = CommenterSerializer()
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentSerializer
        model = Comment
        fields = ("commenter", "content", "date_created", "children")