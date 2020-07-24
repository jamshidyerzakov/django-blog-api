from rest_framework import serializers

from accounts.models import User, Author, Reader


class ReaderDetailSerializer(serializers.ModelSerializer):
    """Reader serializer to show subscribers of authors"""

    url = serializers.HyperlinkedIdentityField(view_name="account:reader-detail")

    class Meta:
        model = Reader
        fields = ('id',
                  'email',
                  'url'
                  )


class ReaderSerializer(serializers.ModelSerializer):
    """Reader serializer to create, retrieve a reader and get list of readers"""

    url = serializers.HyperlinkedIdentityField(view_name="account:reader-detail")

    class Meta:
        model = Reader
        fields = ('id',
                  'email',
                  'password',
                  'first_name',
                  'last_name',
                  'img',
                  'liked_posts',
                  'subscribed_categories',
                  'subscribed_authors',
                  'is_staff',
                  'is_active',
                  'is_superuser',
                  'is_author',
                  'last_login',
                  'url'
                  )

    def create(self, validated_data):
        return Reader.objects.create_reader(**validated_data)

    def validate_is_superuser(self, value):
        """Check whether Reader object is not superuser"""
        if value is True:
            raise serializers.ValidationError("Reader must not have is_superuser=True")
        return value

    def validate_is_staff(self, value):
        """Check whether Reader object is not staff user"""
        if value is True:
            raise serializers.ValidationError("Reader must not have is_staff=True")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """Author serializer to create, retrieve am author and get list of authors"""

    url = serializers.HyperlinkedIdentityField(view_name="account:author-detail")
    subscribers = serializers.SerializerMethodField('get_author_subscribers')

    class Meta:
        model = Author
        fields = ('id',
                  'email',
                  'password',
                  'first_name',
                  'last_name',
                  'img',
                  'subscribers',
                  'is_staff',
                  'is_active',
                  'is_superuser',
                  'is_author',
                  'last_login',
                  'url'
                  )

    def create(self, validated_data):
        return Author.objects.create_author(**validated_data)

    def get_author_subscribers(self, author_obj):
        """Get all subscribers of author"""
        subscribers = [reader.id for reader in author_obj.subscribed_authors.all()]

        return subscribers


class CustomUserSerializer(serializers.ModelSerializer):
    """User serializer to create, retrieve a user and get list of users"""

    url = serializers.HyperlinkedIdentityField(view_name="account:user-detail")

    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'password',
                  'first_name',
                  'last_name',
                  'is_staff',
                  'is_active',
                  'is_author',
                  'is_superuser',
                  'last_login',
                  'url'
                  )
