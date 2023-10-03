from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile, Moo
from .forms import MooForm,SignupForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    profiles = Profile.objects.all()
    Moos = Moo.objects.all().order_by("-create_at")
    return render(request, 'index.html', {'profiles':profiles, 'Moos':Moos})

def profile(request,pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        Moos = Moo.objects.filter(user_id=pk).order_by("-create_at")

        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST['followname']
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            current_user_profile.save()
            
        return render(request, 'profile.html', {'profile':profile, 'Moos':Moos})
    else:
        return redirect('index')
    
def post(request):
    if request.user.is_authenticated:
        form = MooForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                moo = form.save(commit=False)
                moo.user = request.user
                moo.save()
                return redirect('index')
        return render(request, 'post.html', {'form':form})
    
    else:
        return redirect('index')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            return redirect("login")
    else: 
        return render(request, "login.html",{})

def logout_user(request):
    logout(request)
    return redirect("index")

def register_user(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect("index")
    return render(request, 'register.html', {'form':form})

def moo_like(request, pk):
    if request.user.is_authenticated:
        moo = get_object_or_404(Moo, id=pk)
        if moo.likes.filter(id=request.user.id):
            moo.likes.remove(request.user)
        else:
            moo.likes.add(request.user)
            
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect('index')
