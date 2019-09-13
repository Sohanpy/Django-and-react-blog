from django.urls import path

from .posts.views import AdminListCreate, AdminDeleteupdate
from .users.views import UsersListForAddmin

urlpatterns = [
    path('posts', AdminListCreate.as_view()),
    path('posts/view/<slug>', AdminDeleteupdate.as_view()),
    path('users', UsersListForAddmin.as_view()),
]
