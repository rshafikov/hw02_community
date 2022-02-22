from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUp

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='user/logged_out.html'
        ),
    path(
        'signup/',
        SignUp.as_view(),
        name='signup'
        ),
]