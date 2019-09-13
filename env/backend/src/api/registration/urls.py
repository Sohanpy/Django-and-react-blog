from django.urls import path

from .views import UserSignUpView

urlpatterns = [
    path('registration', UserSignUpView.as_view())
]
