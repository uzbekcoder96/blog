from django.urls import path
from .views import home_page_view, post_detail_view, all_post_view, about_view, contact_view, register_view, login_view

app_name = 'blog'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('posts/', all_post_view, name='posts'),
    path('post/<int:id>', post_detail_view, name='post_detail'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]