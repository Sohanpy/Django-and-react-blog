from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import AdminListSerializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UsersListForAddmin(ListCreateAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = AdminListSerializers
