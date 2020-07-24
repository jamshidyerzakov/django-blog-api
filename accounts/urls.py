from django.urls import path
from accounts import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('reader', views.ReaderViewSet)
router.register('author', views.AuthorViewSet)

urlpatterns = router.urls
