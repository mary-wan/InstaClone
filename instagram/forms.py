from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    
    
class UserRegisterForm(UserCreationForm):
    email= forms.EmailField(help_text='Required. Enter a valid email address.')
    
    # specify model it will interact with
    class Meta:
        model = User  
        fields= ['username','email','password1','password2']
        
        # help_texts = {
        #     'username': None,
        #     'password1':None,
        #     'password2':None,
            
        #     }


User._meta.get_field('email')._unique = True 