from django.urls import path
from . import views

app_name = 'about'
urlpatterns = [
    path('support/', views.AboutSupportView.as_view(), name='support'),
    path('FAQ/', views.AboutFAQView.as_view(), name='FAQ')
]