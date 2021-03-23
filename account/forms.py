from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password_1 = forms.CharField(widget=forms.PasswordInput())
    password_2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', )

    def clean_password2(self, *args, **kwargs):
        data = self.cleaned_data

        if data['password_1'] != data['password_2']:
            raise forms.ValidationError("Incorrect password")
        return data['password_2']

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if (not user) or (not user.check_password(password)):
                raise forms.ValidationError('Неверный пароль или логин')
        return super().clean(*args, **kwargs)
