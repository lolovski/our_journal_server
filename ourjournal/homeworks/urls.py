from . import views
from django.urls import path

app_name = 'homeworks'

urlpatterns = [
    path('create/<int:lesson_id>/<str:week>/', views.homework_create, name='homework_create'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('<int:homework_id>/comment', views.add_comment, name='add_comment'),
]