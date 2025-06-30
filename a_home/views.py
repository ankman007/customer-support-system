from django.shortcuts import render

def home_view(request):
    is_guest = not request.user.is_authenticated

    context = {
        "is_guest_session": is_guest
    }
    return render(request, 'home.html', context)
