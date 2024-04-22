from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


app_name = 'api'

router = DefaultRouter()
router.register(r'homeworks', views.HomeworkViewSet, basename='homeworks')
router.register('users', views.UserViewSet)
urlpatterns = [

    path('tg_id_users/', views.TgIdUsersAPI.as_view(), name='tg_id_users'),
    path('shedule/', views.TgSheduleAPI.as_view(), name='schedule'),
    path('', include(router.urls), name='homeworks',),
    path('', include(router.urls), name='users')

]