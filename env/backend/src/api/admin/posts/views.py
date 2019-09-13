from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from posts.models import Post
from .serializers import AdminDetailsSerializers, AdminListSerializers


class AdminListCreate(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = AdminListSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'slug'
    # authentication_classes = (JSONWebTokenAuthentication,)


class AdminDeleteupdate(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = AdminListSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'slug'
    authentication_classes = (JSONWebTokenAuthentication,)
