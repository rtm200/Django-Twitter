from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('post/', views.post, name='post'),
    path('register/', views.register_user, name='register'),
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('moo_like/<int:pk>', views.moo_like, name='moo_like'),
]
