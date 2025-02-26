from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def chat(request):
    messages = Message.objects.all()
    return render(request, 'chat.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('message')
        if content:
            Message.objects.create(user=request.user, content=content)
    return redirect('chatroom')