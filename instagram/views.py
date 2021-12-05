from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect,get_object_or_404
from .models import Image,Profile,Comments
from django.contrib.auth.models import User
from .forms import NewsLetterForm, UserRegisterForm,PostForm,CommentForm
# from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse


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
    comments = Comments.objects.all()
    users =request.user
    current_user = request.user
   
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = current_user
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        post_form = PostForm()
  
    return render(request, 'all-instagram/home.html',{'posts': posts,'post_form': post_form,'users': users,'comments':comments} )



# @login_required(login_url='/accounts/login/')
# def comment(request,image_id):

#     image = get_object_or_404(Image, pk=image_id)
#     current_user =request.user
#     comments =Comments.get_comments_by_images(image_id).all()

#     if request.method == 'POST':
#         image = get_object_or_404(Image, pk = image_id)
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = current_user
#             comment.image = image
#             comment.save()

#     return render(request,'all-instagram/post.html',{'image':image,'comments':comments,'form':form})

def like(request, id):
    post = Image.objects.get(id = id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse("home"))

  

# def post(request,image_id):
#     post = Image.objects.get(id = image_id)
#     comments = Comments.objects.filter(image__id=image_id)
#     current_user = request.user


#     if request.method == "POST":
#         comment_form = CommentForm(request.POST)

#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.user = current_user
#             comment.post = post
#             comment.save()
#             comment_form = CommentForm()
#             return redirect("post", post.image_id)

#     else:
#         comment_form = CommentForm()

#     return render(request, "all-instagram/post.html")

def profile(request):
    return render(request,"all-instagram/profile.html")

@login_required(login_url='login')
def comment(request, id):
    image = get_object_or_404(Image, pk=id)
 
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            savecomment = form.save(commit=False)
            savecomment.post = image
            savecomment.user = request.user
            savecomment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()

    return render(request, 'all-instagram/post.html', {'post': image,'form': form,})

