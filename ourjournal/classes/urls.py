from . import views
from django.urls import path

app_name = 'classes'

urlpatterns = [
    path('', views.index, name='index'),
    path('classes/', views.classes, name='classes'),
    path('classes/<int:pk>/', views.classes_homeworks, name='classes_homeworks'),
    path('classes/<int:class_user_id>/<int:homework_id>/', views.homework_detail, name='homework_detail'),

]