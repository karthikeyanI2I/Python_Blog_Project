from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import BlogData
from django.forms import ModelForm, Textarea


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
            'content': Textarea(attrs={'cols':100,'rows':10}),
        }