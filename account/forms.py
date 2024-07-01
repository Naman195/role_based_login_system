from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={"class": "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    address_line1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    city = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    state = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    pincode = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    is_patient = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input", "data-group": "user-type"}))
    is_doctor = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input", "data-group": "user-type"}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'profile_picture', 'username', 'email', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode', 'is_patient', 'is_doctor')
