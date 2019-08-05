from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as UserLogin,logout as UserLogout,authenticate
from sites.forms import LoginForm


def staticExamples(request):
    return render(request,'site/static_example.html')


def login(request):

    if request.user.username:
        return redirect(dashBoard)
    message=''
    form = LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(username=username,password=password)

            if user is None:
                message='Invalid login details!'
            else:
                UserLogin(request,user)

                request.session['city']='Bangalore'
                request.session['address']='BTM'

                return redirect(dashBoard)

    return render(request,'site/login.html',{
        'form':form,
        'message':message
    })

def registration(request):

    if request.user.username:
        return redirect(dashBoard)

    form=UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=User()
            user.username=form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.save()
    return render(request,'site/registration.html',{'form':form})


def dashBoard(request):

    return render(request,'site/dashBoard.html')

def logout(request):

    UserLogout(request)
    return redirect(login)

def static_page(request):
    return render(request,'site/static_example.html')
