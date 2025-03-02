from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth import logout
from django.shortcuts import redirect


def gra(request):

    profiles = CustomUser.objects.all().order_by('-stosunek')[:14]  # Sortowanie według poprawnych odpowiedzi
    return render(request, 'polls/gra.html', {'users': profiles})
    

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
           
    else:
        form = CustomAuthenticationForm()
    return render(rekwest, 'polls/login.html', {'form': form})


def button_click(request, action):
    if request.user.is_authenticated:
        user = request.user
        if action == 'poprawne':
            user.dobre += 1
        elif action == 'zle':
            user.zle += 1


        user.button_click_count += 1  
        user.save() 
        return redirect('muzyka') 
    else:
        return redirect('muzyka') 



@login_required
def logout_view(request):
    request.session.flush()
    logout(request)
    return redirect('muzyka') 
