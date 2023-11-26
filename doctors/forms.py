from django import forms
from .models import Doctor

class DoctorRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Подтвердите пароль')

    class Meta:
        model = Doctor
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'organization']