from rest_framework import viewsets

from service.general.permissions import get_custom_permissions

from .serializers import(
    CustomUserSerializer,
    ReaderSerializer,
    AuthorSerializer
    )
from .models import User, Reader, Author


class UserViewSet(viewsets.ModelViewSet):
    """
     A viewset that provides `retrieve`, `create`, `list`, `update`,
    `partial update` and `destroy` actions.
    """
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(UserViewSet, self).get_permissions()


class ReaderViewSet(viewsets.ModelViewSet):
    """
     A viewset that provides `retrieve`, `create`, `list`, `update`,
    `partial update` and `destroy` actions.
    """
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

    def get_permissions(self):
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(ReaderViewSet, self).get_permissions()


class AuthorViewSet(viewsets.ModelViewSet):
    """
     A viewset that provides `retrieve`, `create`, `list`, `update`,
    `partial update` and `destroy` actions.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(AuthorViewSet, self).get_permissions()
