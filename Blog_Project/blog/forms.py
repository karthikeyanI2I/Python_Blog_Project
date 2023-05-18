from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import BlogData
from django.forms import ModelForm, Textarea
from django.core.exceptions import ValidationError
import tomllib
config_filepath = 'config.toml'


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class BlogForm(forms.ModelForm):
    class Meta:
        model   = BlogData 
        fields  = ('title', 'content', 'image')
        widgets = {
            'content': Textarea(attrs={'cols':40,'rows':10}),
        }
        
    
    def clean_image(self):
        image_file = self.cleaned_data.get('image') 
        with open(config_filepath, 'rb') as f:            
            data = tomllib.load(f)
            mimage_size = data.get('image_validation')['image_size']
            image_formats = data.get('image_validation')['image_formats']
            image_size_error = data.get('image_validation')['image_size_error']
            image_format_error = data.get('image_validation')['image_format_error']       
        if image_file:
            extension = image_file.name.split(".")[-1]
            if extension not in image_formats:
                raise forms.ValidationError(image_format_error)
            if image_file.size > mimage_size:  # 3MB                
                raise forms.ValidationError(image_size_error)
        return image_file
    
    