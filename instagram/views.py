from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect,get_object_or_404
from .models import Image,Profile,Comments
from django.contrib.auth.models import User
from .forms import NewsLetterForm, UserRegisterForm,PostForm,CommentForm
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


@login_required(login_url='/accounts/login/')
def index(request):
    posts= Image.objects.all()
    
    users = User.objects.exclude(id=request.user.id)
    current_user = request.user
    
    # if 'comment' in request.GET and request.GET["comment"]:
    #     comment=request.GET.get("comment")
    #     comment.save()
        
        
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = current_user
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        post_form = PostForm()
  
    return render(request, 'all-instagram/home.html',{'posts': posts,'post_form': post_form,'users': users} )



@login_required(login_url='/accounts/login/')
def comment(request,image_id):
    #Getting comment form data
    current_user =request.user
    comments =Comments.get_comments_by_images(image_id).all()
    # comments = Comments.objects.filter(image__id=image_id)
    if request.method == 'POST':
        image = get_object_or_404(Image, pk = image_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = image
            comment.save()
        return redirect('home')
    




