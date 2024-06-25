from django.shortcuts import render, redirect
from django.contrib import messages
from .form import BookingForm,BookingRoom
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Review,Booking,Room
from .form import ReviewForm

def home(request):
    return render(request, 'home.html')
@login_required(login_url='/')
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        fore=BookingRoom(request.POST)

        if form.is_valid():
            if fore.is_valid():
                
                form.save()
                fore.save()
                    
                messages.success(request,'....Your Room is booked........')
                return redirect('booking')
        else:
            messages.success(request,"......Room no already taken.......")
            return redirect('booking')        
            
    else:
        
        form = BookingForm()
        p=Booking.objects.all()
    s=Booking.objects.filter(name=request.user)
    return render(request, 'booking.html',{'user': request.user,'s':s,'p':p})

def logoutuser(request):

    logout(request)
    
    return redirect("/")








# Create your views here.

def login25(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password= request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
            
        if user is not None:
            login(request,user)
            messages.success(request,'  You are sucessfully login... ')
          
            return redirect("booking")
        if request.user is login:
            return redirect('/')    
        else:
            messages.error(request,' username or password is wrong')
            return render(request,'login.html')
        
    
    
    return render(request,'login.html')
        

   


def SignupPage(request):
    
    if request.method=='POST':
        
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        print(uname,email,pass1)
        
            
        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                
                messages.error(request,' username already taken')
                return redirect('signup.html')
            
            elif User.objects.filter(email=email).exists():
                
                messages.error(request,' email already taken')
                return redirect('signup.html')
            else:
                user=User.objects.create_user(uname,email,pass1)
                user.save()
                messages.success(request,' your form is registered')
        
            
                return redirect('login.html')
        else:
            messages.error(request,'password not matching')
            return redirect('signup.html')

        
    else:
        return render(request,'signup.html')
def logoutuser(request):
    logout(request)
    
    return redirect("/")




def index(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        print(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.rating = request.POST.get('rating')
            review.name=request.user
            form.save()
            
            
            return redirect('index.html')  # Redirect to a success page
    else:
        form = ReviewForm()

        reviews= Review.objects.all()
        

    return render(request, 'index.html',{'reviews':reviews })
def edit(request,id):
    user=Booking.objects.get(id=id)
    if request.method=='POST':
        
        
    
        user.name=request.POST.get('name')
        user.email=request.POST.get('email')
        user.phone=request.POST.get('phone')
        user.room_type=request.POST.get('room_type')
        user.check_in=request.POST.get('check_in')
        user.check_out=request.POST.get('check_out')
        user.number=request.POST.get('number')
        user.save()
        messages.success(request,"........sucessfully updated........")
        return redirect("booking")
    
    
    return render(request,"edit.html",{'user':user})

def delete(request,id):
    user=Booking.objects.get(id=id)
    user.delete()
    messages.success(request,"......Sucessfully Cancled booking.......")
    return redirect("booking")
def admin(request):
    return render(request,"admin.html")



    




        
     





