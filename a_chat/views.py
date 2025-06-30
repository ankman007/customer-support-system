from django.shortcuts import render
from loguru import logger

def chat(request):
    is_guest = not request.user.is_authenticated
    context = {
        "is_guest_session": is_guest,
        "user": request.user if not is_guest else None
    }
    return render(request, 'chat/guest-session.html', context)