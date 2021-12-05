from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200, blank=True)
    caption = models.CharField('Caption(optional)', max_length=3000, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
        
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.caption

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default=" Add Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)

    def __str__(self):
        return {self.user.username} 

    
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return {self.post} 

    class Meta:
        ordering = ["-pk"]
