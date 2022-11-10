from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, KhojForm
# Create your views here.

def RegisterPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'khoj_app/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            
    context = {}
    return render(request, 'khoj_app/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def Home(request):
    form = KhojForm()

    if request.method == 'POST':
        form = KhojForm(request.POST)
        if form.is_valid():
            input_value = form.cleaned_data.get('input_value')
            print(input_value)
            value = form.save(commit=False)
            value.input_value = input_value
            value.user = request.user
            value.save()

    context = {'form': form}
    return render(request, 'khoj_app/home.html', context)
    