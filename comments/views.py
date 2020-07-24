from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from service.general.permissions import get_custom_permissions

from comments.models import Comment
from utils.serializers import get_serializer_by_action
from .serializers import (
    CommentCreateSerializer,
    CommentSerializer,
)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Comment viewset that provides `retrieve`, `create`, `list`, `update`,
    `partial update` and `destroy` actions. Permissions are set to the HTTP methods
    accordingly.
    """
    queryset = Comment.objects.all()
    filter_backends = (DjangoFilterBackend,)

    def get_permissions(self):
        """Specific permissions for specific HTTP query method."""
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(CommentViewSet, self).get_permissions()

    def get_serializer_class(self):
        """Specific serializer for each specific action."""
        return get_serializer_by_action(
            action=self.action,
            serializers={
                'list': CommentSerializer,
                'retrieve': CommentSerializer,
                'create': CommentCreateSerializer,
                'update': CommentSerializer,
                'partial_update': CommentSerializer,
                'metadata': CommentSerializer,
            }
        )
