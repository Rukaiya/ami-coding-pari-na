from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, KhojForm

# user registration


def RegisterPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        if form.error_messages :
            print(form.errors.as_data())
        else:
            return redirect('register')
    context = {'form': form}
    return render(request, 'khoj_app/register.html', context)

# user login

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
                return redirect('login')
            
        return render(request, 'khoj_app/login.html')

# user logout
def logoutUser(request):
    logout(request)
    return redirect('login')

# home page for logged in user
@login_required(login_url='login')
def Home(request):
    form = KhojForm()

    if request.method == 'POST':
        form = KhojForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            input_value = form.cleaned_data.get('input_value')
            search_value = form.data.get('search_value')
            
            # sort the input value and save with user information
            data.input_value = sorted(input_value, reverse=True)
            data.user = request.user
            data.save()
           
            # check if the search value is within input value field 
            if int(search_value) in input_value:
                result = True
            else:
                result = False
      
            if request.headers.get('Hx-Request') == 'true':
                # return only the result to be replaced
                return HttpResponse(str(result))
        else:
            return HttpResponse('Invalid Form Value')
    context = {'form': form}
    return render(request, 'khoj_app/home.html', context)
    