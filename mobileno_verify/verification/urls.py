from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('send-otp/',views.send_otp, name='send_otp'),

    path('', views.index, name='index'),
    path('register/', views.register),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html')),
]


