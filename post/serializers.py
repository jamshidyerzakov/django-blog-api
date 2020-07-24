from rest_framework import serializers

from service.general.serializers import RecursiveSerializer
from service.post.serializers import (
    FilterCategorySerializer,
    TagListSerializer,
)

from post.models import Post, Category
from accounts.serializers import AuthorSerializer
from comments.serializers import CommentSerializer


class PostIdSerializer(serializers.ModelSerializer):
    """Retrieving only id of the post"""

    class Meta:
        model = Post
        fields = ('id', 'url')


class CategoryIdSerializer(serializers.ModelSerializer):
    """Retrieving only id of the category"""

    class Meta:
        model = Category
        fields = ('id', 'url')


class CategorySerializer(serializers.ModelSerializer):
    """Detail serializer for the Category model"""
    children = RecursiveSerializer(many=True)
    posts = PostIdSerializer(many=True)
    subscribed_readers = serializers.SerializerMethodField('get_subscribed_readers')

    class Meta:
        list_serializer_class = FilterCategorySerializer
        model = Category
        fields = ("id", "title", "description", "img", 'subscribed_readers', "children", "posts", "url")

    def get_subscribed_readers(self, category_obj):
        """Get all subscribed readers' id to the current category"""
        subscribers = [reader.id for reader in category_obj.subscribed_categories.all()]

        return subscribers


class CategoryCreateSerializer(serializers.ModelSerializer):
    """General serializer for the Category model"""

    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Detail serializer for the Post model"""
    category = CategoryIdSerializer(read_only=True)
    author = AuthorSerializer(read_only=True)
    comments = CommentSerializer(many=True)
    liked_readers = serializers.SerializerMethodField('get_liked_readers')
    tags = serializers.SerializerMethodField('get_tags')
    url = serializers.HyperlinkedIdentityField(view_name='post-detail')

    class Meta:
        model = Post
        fields = '__all__'

    def get_liked_readers(self, post_obj):
        """Get all readers' id who liked current post"""
        readers = [reader.id for reader in post_obj.liked_posts.all()]

        return readers

    def get_tags(self, post_obj):

        tags = [tag.name for tag in post_obj.tags.all()]

        return tags


class PostCreateSerializer(serializers.ModelSerializer):
    """General serializer for the Post model"""
    tags = TagListSerializer(required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        return Post.objects.create_post(**validated_data)

