from django.urls import path

from .user_profile.views import UserProfileView, UserStatusView

urlpatterns = [
    path('profile', UserProfileView.as_view()),
    path('user_status', UserStatusView.as_view())
]
