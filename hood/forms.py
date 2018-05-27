from django  import forms
from .models import Neighborhood,Business,MyUser,Post

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        exclude = ['user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['editor','post_date']
