from django.shortcuts import render
from .models import Destination
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    des = Destination.objects.all() 

    return render(request,"index.html",{'des':des})




def register(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user has use')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'email has use')
                 return redirect('register')
            else:
                user = User.objects.create_user(username = username ,password=pass1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('home')
                

        else:
             print('password not matching...')
             return redirect('register')

        return redirect('/')
    return render(request,"register.html")

    