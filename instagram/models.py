from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(max_length=400, default="Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    profile_pic = models.ImageField(upload_to='images/',default='v1638711191/images/default_qu1pfb.png')
   

    def __str__(self):
        return f'{self.user.username}'

 

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField('Caption(optional)', max_length=300, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='images')
    # profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True) 
    likes = models.IntegerField(default=0)

    
    
    class Meta:
        ordering = ['-upload_date']

    
    def __str__(self):
        return f'{self.user.username} Image'

 
class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'
        

class Comments(models.Model):
    comment = models.TextField(max_length = 300)
    image = models.ForeignKey(Image,null=True, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True) 
    
    
    class Meta:
        ordering = ["-comment_date"]


    def __str__(self):
        return f'{self.user.name} Image'

