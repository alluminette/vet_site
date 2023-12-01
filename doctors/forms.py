from django import forms
from .models import Doctor


class AgreementField(forms.BooleanField):
    def __init__(self, *args, **kwargs):
        self.agreement_text = kwargs.pop('agreement_text', '')
        super().__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs['data-agreement-text'] = self.agreement_text
        return attrs
    

class DoctorRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Подтвердите пароль')

    privacy_agreement_page = AgreementField(
        label='Согласие на обработку персональных данных',
        agreement_text='Текст согласия на обработку персональных данных'
    )

    oferta_agreement_page = AgreementField(
        label='Согласие на оферту',
        agreement_text='Текст согласия на условия взаимодействия'
    )

    class Meta:
        model = Doctor
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'organization']