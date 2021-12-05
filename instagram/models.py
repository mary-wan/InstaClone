from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='images/')
    pub_date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name

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

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField('Caption(optional)', max_length=300, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    upload_date = models.DateTimeField(auto_now_add=True) 
    
    
    
    class Meta:
        ordering = ['-upload_date']
    
    # def __unicode__(self):
    #     try:
    #         public_id = self.image.public_id
            
    #     except AttributeError:
    #         public_id = ""
    #     return "Photo <%s:%s>" % (self.caption,public_id)
    
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
