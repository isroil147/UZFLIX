from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def video(request):
    obj = Item.objects.all()
    return render(request, 'home.html', {'obj':obj})


def home(request):
    products = Item.objects.all()
    categories = Category.objects.all()
    context = {'products':products, 'categories':categories}
    return render(request, 'video.html', context)

def detail(request, id):
    product = Movie.objects.get(pk=id)
    product = get_object_or_404(Movie, pk=id)
    return render (request, 'vid_det.html', {'product':product})
def signup(request):
        if request.method=="POST":
            username=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('pass1')
            pass2=request.POST.get('pass2')
        
            if len(username)>25:
                messages.info(request,"Username Must be 25 Digits")
                return redirect('/signup')

            if pass1!=pass2:
                messages.info(request,"Password is not Matching")
                return redirect('/signup')
        
            try:
                if User.objects.get(username=username):
                    messages.warning(request,"Username is Taken")
                    return redirect('/signup')
            
            except Exception as identifier:
                pass
            
            
            try:
                if User.objects.get(email=email):
                    messages.warning(request,"Email is Taken")
                    return redirect('/signup')
            
            except Exception as identifier:
                pass
            
            
            
            myuser=User.objects.create_user(username,email,pass1)
            myuser.save()
            messages.success(request,"User is Created Please Login")
            return redirect('/login')
            
            
        return render(request,"signup.html")




def handlelogin(request):
        if request.method=="POST":        
            username=request.POST.get('username')
            pass1=request.POST.get('pass1')
            myuser=authenticate(username=username,password=pass1)
            if myuser is not None:
                login(request,myuser)
                messages.success(request,"Login Successful")
                return redirect('/')
            else:
                messages.error(request,"Invalid Credentials")
                return redirect('/login')
                
            
        return render(request,"login.html")


def logoutfunction(request):
    logout(request)
    return redirect('/signup')












def UserProfile(request, username):
    Profile.objects.get_or_create(user=request.user)
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)

    context = {
        'profile':profile,
      }
    return render(request, 'profile.html', context)


def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = Result.objects.filter(name__icontains=query)
            return render(request, 'search_result.html', {'results': results})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})

def results(request, pk):
    product = Result.objects.get(pk=pk)
    context = {'product':product}
    return render (request, 'search_result.html', context)


