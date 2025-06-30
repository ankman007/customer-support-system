from django.urls import path
from a_chat.views import chat

urlpatterns = [
    path('', chat, name="chat"),
]
