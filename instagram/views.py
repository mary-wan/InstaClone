from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect,get_object_or_404
from .models import Follow, Image,Profile,Comments
from django.contrib.auth.models import User
from .forms import NewsLetterForm, UpdateUserForm, UpdateUserProfileForm, UserRegisterForm,PostForm,CommentForm
# from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse



@login_required(login_url='/accounts/login/')
def index(request):
    posts= Image.objects.all()
    comments = Comments.objects.all()
    all_users = User.objects.exclude(id=request.user.id)
    current_user = request.user
    
    
   
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        post_form = PostForm()
  
    return render(request, 'all-instagram/home.html',{'posts': posts,'post_form': post_form,'all_users': all_users,'comments':comments,'current_user':current_user} )


def register(request):
    if request.user.is_authenticated:
    #redirect user to the profile page
        return HttpResponseRedirect(index)
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


@login_required(login_url='login')
def profile(request, username):
    images = request.user.images.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user.profile)
        profile_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserProfileForm()

    return render(request, 'all-instagram/profile.html', {'user_form':user_form,'profile_form':profile_form,'images':images})


@login_required(login_url='login')
def comment(request, id):
    image = Image.objects.get(id=id)
    comments = Comments.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.image = image
            new_comment.user = request.user.profile
            new_comment.save()
            
            return HttpResponseRedirect(request.path_info)
            
    else:
        form = CommentForm()

    return render(request, 'all-instagram/post.html', {'post': image,'form': form,'comments':comments})

@login_required(login_url='login')
def unfollow(request, to_unfollow):
    if request.method == 'GET':
        unfollow_profile = Profile.objects.get(pk=to_unfollow)
        new_unfollowed = Follow.objects.filter(follower=request.user.profile, followed=unfollow_profile)
        new_unfollowed.delete()
        return redirect('user_profile', unfollow_profile.user.username)

@login_required(login_url='login')
def follow(request, to_follow):
    if request.method == 'GET':
        follow_profile = Profile.objects.get(pk=to_follow)
        new_following = Follow(follower=request.user.profile, followed=follow_profile)
        new_following.save()
        return redirect('user_profile', follow_profile.user.username)
    
    
@login_required(login_url='login')
def user_profile(request, username):
    user_poster = get_object_or_404(User, username=username)
    if request.user == user_poster:
        return redirect('profile', username=request.user.username)
    user_posts = user_poster.images.all()
    
    followers = Follow.objects.filter(followed=user_poster.profile)
    if_follow = None
    for follower in followers:
        if request.user.profile == follower.follower:
            if_follow = True
        else:
            if_follow = False

    print(followers)
    return render(request, 'all-instagram/poster.html', {'user_poster': user_poster,'followers': followers, 'if_follow': if_follow,'user_posts':user_posts})


@login_required(login_url='login')
def like(request, id):
    post = Image.objects.get(id = id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse("home"))

@login_required(login_url='login')
def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        print(results)

        return render(request, 'all-instagram/users.html',locals())

    return redirect(index)

