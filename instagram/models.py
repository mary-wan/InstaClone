from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile', null=True)
    bio = models.CharField(max_length=200, default="Bio")
    profile_pic = models.ImageField(upload_to='images/',default='v1638711191/images/default_qu1pfb.png')

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles
    
    @classmethod
    def search_by_username(cls,search_term):
        profiles = cls.objects.filter(title__icontains=search_term)
        return profiles
    @receiver(post_save, sender=User)
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance) 
            
    def __str__(self):
        return self.bio 

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField('Caption(optional)', max_length=300, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    upload_date = models.DateTimeField(auto_now_add=True) 
    likes = models.IntegerField(default=0)

    
    
    class Meta:
        ordering = ['-upload_date']

    
    def __str__(self):
        return self.caption
    

class Comments(models.Model):
    comment = models.CharField(max_length = 300)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    comment_date = models.DateTimeField(auto_now_add=True) 
    
    
    class Meta:
        ordering = ["-comment_date"]

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments 
    
    def __str__(self):
        return self.comment

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'