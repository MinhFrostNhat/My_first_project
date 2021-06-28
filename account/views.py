from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import order
from .models import cart1
import zipfile
from django.http import HttpResponse

# Create your views here.
def order1(request):
    des = order.objects.all() 

    return render(request,"order.html",{'des':des})
    
    
def cart(request):
    if request.method=='POST':
        user_name=request.POST["user_name"]
        user_address=request.POST["user_address"]
        user_price=request.POST["user_price"]
        user_product=request.POST["user_product"]
        user_file=request.POST["user_file"]
        cart=cart1(user_name=user_name,user_address=user_address, user_price=user_price,user_product=user_product,user_file=user_file)
        cart.save();
        messages.info(request,'ok')
        return redirect('cart')
    else:
        return render(request,'cart.html')
    
def final(request):
    cart2 =cart1.objects.all()
    return render(request,"final.html",{'cart2':cart2})

    
def home(request):
    return render(request,'home.html')
    
def handle_uploaded_file(f):
    with open('"../media/hinhanh'+f.name,'wb+') as defs:
        for concac in f.concac():
            defs.write(concac)

def download(request):
    cart11=cart1()
    if request.method=="POST":
        cart11=cart1(request.POST,request.FILES)
        if cart11.user_file:
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File")
        else:
            cart11=cart1()
    return render(request,'download.html',{'cart11':cart11})
    

















    
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("home")
            else:
                    messages.info(request,'invalid') 
                    return redirect('login')
        else:
            return render(request,'login.html')





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

    
    
    