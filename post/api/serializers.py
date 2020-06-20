from rest_framework import serializers
from post.models import Post, Category
from accounts.models import User
from rest_framework.exceptions import ParseError
from ..service import RecursiveSerializer
from comments.api.serializers import CommentSerializer

# class Base64ImageField(serializers.ImageField):
#     """
#     A Django REST framework field for handling image-uploads through raw post data.
#     It uses base64 for encoding and decoding the contents of the file.
#
#     Heavily based on
#     https://github.com/tomchristie/django-rest-framework/pull/1268
#
#     Updated for Django REST framework 3.
#     """
#
#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid
#
#         # Check if this is a base64 string
#         if isinstance(data, six.string_types):
#             # Check if the base64 string is in the "data:" format
#             if 'data:' in data and ';base64,' in data:
#                 # Break out the header from the base64 content
#                 header, data = data.split(';base64,')
#
#             # Try to decode the file. Return validation error if it fails.
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')
#
#             # Generate file name:
#             file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
#             # Get the file name extension:
#             file_extension = self.get_file_extension(file_name, decoded_file)
#
#             complete_file_name = "%s.%s" % (file_name, file_extension, )
#
#             data = ContentFile(decoded_file, name=complete_file_name)
#
#         return super(Base64ImageField, self).to_internal_value(data)
#
#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr
#
#         extension = imghdr.what(file_name, decoded_file)
#         extension = "jpg" if extension == "jpeg" else extension
#
#         return extension
#


class FilterCommentSerializer(serializers.ListSerializer):
    """Filtering comments, only parents"""
    def to_representation(self, data):
        data = data.filter(reply_to=None)
        return super().to_representation(data)


class FilterCategorySerializer(serializers.ListSerializer):
    """Filtering comments, only parents"""
    def to_representation(self, data):
        data = data.filter(parent_category=None)
        return super().to_representation(data)


class AuthorDetailSerializer(serializers.ModelSerializer):
    """Displaying a single User"""

    class Meta:
        model = User
        fields = '__all__'


class PostIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', )


class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)
    posts = PostIdSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCategorySerializer
        model = Category
        fields = ("id", "category_title", "description", "children", "posts")


class CategoryListSerializer(serializers.ModelSerializer):
    """Displaying list of categories"""

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Displaying a single category"""

    class Meta:
        model = Category
        fields = '__all__'


class TagListSerializer(serializers.ListField):
    def from_native(self, data):
        if type(data) is not list:
            raise ParseError("expected a list of data")
        return data

    def to_native(self, obj):
        return obj.all()

    #
    # def create(self, validated_data):
    #     tags = validated_data.pop('tags')
    #     instance = super(TagSerializer, self).create(validated_data)
    #     instance.tags.set(*tags)
    #     return instance


class PostListSerializer(serializers.ModelSerializer):
    """Displaying list of posts"""
    category = CategorySerializer()
    author = AuthorDetailSerializer(read_only=True)
    comments = CommentSerializer(many=True)
    tags = serializers.SlugRelatedField(many=True, queryset=Post.tags.all(), slug_field="name")

    class Meta:
        model = Post
        fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    """Displaying a single post"""
    category = CategorySerializer()
    author = AuthorDetailSerializer(read_only=True)
    comments = CommentSerializer(many=True)
    tags = serializers.SlugRelatedField(many=True, queryset=Post.tags.all(), slug_field="name")

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    """Displaying a single post"""
    tags = TagListSerializer()
    # img = Base64ImageField(
    #     max_length=None, use_url=True, required=True
    # )

    class Meta:
        model = Post
        fields = '__all__'
