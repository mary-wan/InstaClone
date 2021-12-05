from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Image
# from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    
    
class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    
    # specify model it will interact with
    class Meta:
        model = User  
        fields= ['username','email','password1','password2']
        
        help_texts = { 'username': None, 'password2': None, }


User._meta.get_field('email')._unique = True 

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'caption')
       
# class CommentForm(forms.ModelForm):
#     comment = forms.CharField(label='Leave a comment',max_length=30)

#     class Meta:
#         model = Comment
#         fields = ('comment',)