from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Post, Vote
from django.utils.timezone import now  
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Post
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import JsonResponse

def gra(request):
    if request.user.is_authenticated:
        profiles = CustomUser.objects.all().order_by('-stosunek')  # Sortowanie według poprawnych odpowiedzi
        return render(request, 'polls/gra.html', {'users': profiles})
    else:
        return render(request, 'polls/gra.html')

def register(rekwest):
    if rekwest.method == 'POST':
        form = CustomUserCreationForm(rekwest.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(rekwest, 'polls/register.html', {'form': form})

def user_login(rekwest):
    if rekwest.method == 'POST':
        form = CustomAuthenticationForm(rekwest.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(rekwest, username=username, password=password)
            if user is not None:
                login(rekwest, user)
                return redirect('muzyka')  
            else:
                form.add_error(None, 'a')
        else:
            print(form.errors)
            print("kurde")
           
    else:
        form = CustomAuthenticationForm()
    return render(rekwest, 'polls/login.html', {'form': form})


def button_click(request, action):

    user = request.user
    if action == 'poprawne':
        user.dobre += 1
    elif action == 'zle':
        user.zle += 1


    user.button_click_count += 1  
    user.save() 
    messages.success(request, f'Liczba kliknięć: {user.button_click_count}')
    return redirect('muzyka') 

from .models import CustomUser


