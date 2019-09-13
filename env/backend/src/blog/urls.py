from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token', obtain_jwt_token),
    path('rest-auth/', include('rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title='Blog API Documentation')),
    path('api/v1/posts/', include('api.posts.urls')),
    path('api/v1/comments/', include('api.comments.urls')),
    path('api/v1/dashboard/', include('api.dashboard.urls')),
    path('api/v1/users/', include('api.registration.urls')),
    path('api/v1/admin-control/', include('api.admin.urls')),
]
