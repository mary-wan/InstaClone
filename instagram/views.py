from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect
# from .models import Article,NewsLetterRecipients
from .forms import NewsLetterForm, UserRegisterForm
# from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'all-instagram/home.html')

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