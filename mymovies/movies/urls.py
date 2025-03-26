from django.urls import path
from django.contrib.auth import views as auth_views
from .views import movie_list, register, movie_detail

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='movies/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
