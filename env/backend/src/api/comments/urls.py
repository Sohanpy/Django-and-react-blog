from django.urls import path

from .views import comment_list_view, comment_create_view

urlpatterns = [
    path('<slug>', comment_list_view),
    path('create/<slug>', comment_create_view)
]
