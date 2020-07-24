from rest_framework.routers import DefaultRouter
from post import views


router = DefaultRouter()
router.register('post', views.PostViewSet)
router.register('category', views.CategoryViewSet)

urlpatterns = router.urls
