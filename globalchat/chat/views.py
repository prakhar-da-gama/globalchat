# chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .models import Message
from .pos_analysis import analyze_sentence

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('post_message')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_message')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def post_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        analyze_sentence(content)
        Message.objects.create(user=request.user, content=content)
    messages = Message.objects.all()
    return render(request, 'post_message.html', {'messages': messages})
