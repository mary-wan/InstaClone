from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect,get_object_or_404
from .models import Image,Profile
from django.contrib.auth.models import User
from .forms import NewsLetterForm, UserRegisterForm,PostForm
# from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
            
    else:
        form = UserRegisterForm()
    return render(request,"registration/register.html",{'form':form})


def index(request):
    posts= Image.objects.all()
    
    users = User.objects.exclude(id=request.user.id)
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
  
    return render(request, 'all-instagram/home.html',{'posts': posts,'form': form,'users': users} )




