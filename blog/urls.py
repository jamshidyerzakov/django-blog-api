from django.contrib import admin
from django.urls import path, include
from django.conf import settings

import accounts
from .yasg import urlpatterns as doc_urls
from django.conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/api/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),

    path('', include('post.urls')),
    path('', include(('accounts.urls', "accounts"), namespace="account")),
    path('', include('comments.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('rest_framework_social_oauth2.urls')),

]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)