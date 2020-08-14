from . import  views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='Home'),
    path('logout/', views.log_out, name="logout"),
    path('createpoll/', views.create_poll, name="createpoll"),
    path('vote/<int:id>/', views.vote, name="vote"),
    path('result/<int:id>/', views.result, name="result"),
]