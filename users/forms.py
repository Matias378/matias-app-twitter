from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()#si no pongo nada, es campo requerido (required= False) sino

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2'] #aca elijo que campos quiero y en que orden, mejora como se ve el formulario por defecto

class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']

