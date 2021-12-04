from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField('Caption(optional)', max_length=3000, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True) 
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    
    # def __unicode__(self):
    #     try:
    #         public_id = self.image.public_id
            
    #     except AttributeError:
    #         public_id = ""
    #     return "Photo <%s:%s>" % (self.caption,public_id)
        
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.caption
