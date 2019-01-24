
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html', {})

@login_required
def room(request, room_name):
    users = User.objects.all()
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'users':users,
        'login_user': request.user
    })