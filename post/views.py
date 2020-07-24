from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from service.post.filters import PostFilter
from service.post.pagination import PostPagination
from service.general.permissions import get_custom_permissions

from utils.serializers import get_serializer_by_action

from post.models import Post, Category
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
    CategorySerializer,
    CategoryCreateSerializer,
)


class PostViewSet(ModelViewSet):
    """
     Post viewset that provides `retrieve`, `create`, `list`, `update`,
    `partial update` and `destroy` actions.
    """
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostFilter
    pagination_class = PostPagination
    queryset = Post.objects.all()

    def get_permissions(self):
        """Specific permissions for specific HTTP query method."""
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(PostViewSet, self).get_permissions()

    def get_serializer_class(self):
        """Specific serializer for specific action."""
        return get_serializer_by_action(
            action=self.action,
            serializers={
                'list': PostSerializer,
                'retrieve': PostSerializer,
                'create': PostCreateSerializer,
                'update': PostSerializer,
                'partial_update': PostSerializer,
                'metadata': PostSerializer
            }
        )


class CategoryViewSet(ModelViewSet):
    """
    Category viewset that provides `retrieve`, `create`, `list`, `update`,
    `partial update` and `destroy` actions.
    """
    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend,)

    def get_permissions(self):
        """Specific permissions for specific HTTP query method."""
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(CategoryViewSet, self).get_permissions()

    def get_serializer_class(self):
        """Specific serializer for specific action."""
        return get_serializer_by_action(
            action=self.action,
            serializers={
                'list': CategorySerializer,
                'retrieve': CategorySerializer,
                'create': CategoryCreateSerializer,
                'update': CategorySerializer,
                'partial_update': CategorySerializer,
                'metadata': CategorySerializer,
            }
        )
