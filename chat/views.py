from django.shortcuts import render,redirect
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        user_data = request.POST.dict()
        print(user_data)
        username = user_data.get("Username")
        group = user_data.get("Group")
        request.session[0] = username
        # response = HttpResponse()
        # response.set_cookie('username',username)
        return redirect('room',room_name=group)
    else:

        return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name, 'chatuser':request.session['0']
    })