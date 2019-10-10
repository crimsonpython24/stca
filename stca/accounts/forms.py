from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User

# Create your forms here
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class UserSettingForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'text', 'avatar']