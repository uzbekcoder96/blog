from django.urls import path
from .views import  register_view, login_view, logout_view, verify_email_view

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('<int:user_id>/verify/<str:token>', verify_email_view, name='verify-email'),
]