from django.urls import path
from . import views

app_name = 'about'
urlpatterns = [
    path('support/', views.AboutSupportView.as_view(), name='support'),
    path('FAQ/', views.AboutFAQView.as_view(), name='FAQ'),
    path('chat_bot_info/', views.AboutChatBotView.as_view(), name='chat_bot_info')
]