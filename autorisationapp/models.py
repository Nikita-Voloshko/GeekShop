from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone

# Create your models here.


class User(AbstractBaseUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    age = models.PositiveSmallIntegerField(),
    first_name = models.CharField(blank=True, max_length=30, verbose_name='first_name'),
    last_name = models.CharField(blank=True, max_length=150, verbose_name='last_name'),
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                                  help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                  max_length=150, unique=True,
                                  validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                                  verbose_name='username')
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address')
