from autorisationapp.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


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
        field = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(registerUser, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию пользователя'
        self.fields['username'].widget.attrs['placeholder'] = 'Введите ник пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите почту'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
