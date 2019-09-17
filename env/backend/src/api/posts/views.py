from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .serializers import PostsSerializers, PostDetailsSerializers
from posts.models import Post


class PostsListView(ListAPIView):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostsSerializers
    lookup_field = 'slug'


class PostsDetailsView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailsSerializers
    lookup_field = 'slug'
