from django.urls import path

from .views import PostsListView, PostsDetailsView

urlpatterns = [
    path('list', PostsListView.as_view()),
    path('list/<slug>', PostsDetailsView.as_view())
]
