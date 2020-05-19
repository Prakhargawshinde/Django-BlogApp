from django import forms
from Blog_App.models import Post_blog_form
from django.contrib.auth.models import User
class Blog_signup(forms.ModelForm):
    """docstring for Blog_signup."""
    class Meta:
        model = User
        #fields = "__all__"
        fields = ('username','password','email','first_name','last_name')
        widgets={'password':forms.PasswordInput()}
class Post_blog(forms.ModelForm):
    class Meta:
        model = Post_blog_form
        fields = ('Title','Description','Pic')
