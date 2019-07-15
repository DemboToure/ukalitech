from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required , user_passes_test
from .forms import loginform
# Create your views here.

# following function are called by user_passes_test
# for testing if user can acces on one url or no 
def is_not_conected(user):
    return not user.is_authenticated

# end functions 



def home(request):
    
    return render(request, 'default.html')


@user_passes_test(is_not_conected, login_url='/website/dashboard')
def login_user(request):
    form = loginform(request.POST or None ) 
    if form.is_valid():
        username = request.POST.get('username') 
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request, user)
            print("succesfuly authenticated")
            return redirect('dashboard')
        else:
            print('authentication fail')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')

@login_required(login_url='/website/login_user')
def dashboard(request):

    return render(request, 'dashboard.html')

@login_required(login_url='/website/login_user')
def applications(request):

    return render(request, 'applications.html')

