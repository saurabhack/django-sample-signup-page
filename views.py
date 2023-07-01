from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import paste
# Create your views here.
def index(request):
    yess=paste.objects.all()
    return render(request,'index.html',{'yess':yess})
    #at=info.objects.all()

#{'adds':adds}

def profile(request):
    text2=request.POST['text2']
    text3=request.POST['text3']
    return render(request,'profile.html' ,{'text2':text2 ,'text3':text3})


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password does not matched')   
            return redirect('register')
    else:
        return render(request,'register.html')


