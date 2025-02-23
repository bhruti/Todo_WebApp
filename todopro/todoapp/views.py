from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    if(request.method == "POST"):
        task=request.POST.get('task')
        if(len(task)==0):
            return redirect('home-page')
        new_todo=todo(user=request.user,task=task)
        new_todo.save()
    all_tasks=todo.objects.filter(user=request.user)
    username=request.user.username
    context={
        'username':username,
        'todos':all_tasks
    }
    return render(request, 'todoapp/todo.html', context)

def register(request):
    if(request.user.is_authenticated):
        return redirect('home-page')
    if(request.method == 'POST'):
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        get_user_by_email=User.objects.filter(email=email)
        if(get_user_by_email):
            messages.error(request,'Email already registered. Please use different email id.')
            return redirect('register')

        if(len(password) < 8):
            messages.error(request,'Password must be atleast 8 characters long')
            return redirect('register')

        new_user = User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request, 'User created successfully. Login now.')
        return redirect('login')

    return render(request, 'todoapp/register.html', {})

def loginpage(request):
    if(request.user.is_authenticated):
        return redirect('home-page')
    if(request.method == 'POST'):
        username=request.POST.get('uname')
        password=request.POST.get('pass')

        validate_user=authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('home-page')
        else:
            # print(username,password)
            messages.error(request,'Incorrect details or the user doesnot exist.')
            return redirect('login')

    return render(request, 'todoapp/login.html', {})

@login_required
def delete_task(request, name):
    del_task=todo.objects.get(user=request.user,task=name)
    del_task.delete()
    return redirect('home-page')

@login_required
def update_task(request, name):
    upd_task=todo.objects.get(user=request.user,task=name)
    print(upd_task.is_complete)
    upd_task.is_complete=True
    upd_task.save()
    print(upd_task.is_complete)
    return redirect('home-page')

def logoutview(request):
    logout(request)
    messages.success(request, 'logged out successfully.')
    return redirect('login')

def pass_reset(request):
    return render(request,'todoapp/pass_reset.html')