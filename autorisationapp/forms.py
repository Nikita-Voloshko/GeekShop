from autorisationapp.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms


class loginUser(AuthenticationForm):
    class Meta:
        model = User
        field = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(loginUser, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите ник пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        for field_name, field in self.files.items():
            field.widget.attrs['class'] = 'form-control py-4'


class registerUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(registerUser, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите адрес эл. почты'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class ChangeProfil(UserChangeForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar','first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(registerUser, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
