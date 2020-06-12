from rest_framework import serializers
from post.models import Post, Comment, Category
from accounts.models import User
from rest_framework.exceptions import ParseError


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


class RecursiveSerializer(serializers.Serializer):
    """Recursive display of children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class AuthorDetailSerializer(serializers.ModelSerializer):
    """Displaying a single User"""

    class Meta:
        model = User
        fields = '__all__'


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



class TagListSerializer(serializers.ListField):
    def from_native(self, data):
        if type(data) is not list:
            raise ParseError("expected a list of data")
        return data

    def to_native(self, obj):
        return obj.all()


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

    class Meta:
        model = Post
        fields = '__all__'
