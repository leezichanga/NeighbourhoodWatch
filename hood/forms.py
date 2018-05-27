from django  import forms

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        exclude = ['user']
