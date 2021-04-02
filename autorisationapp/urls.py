from django.urls import path

from autorisationapp.views import login, register, logout

app_name = 'autorisationapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
