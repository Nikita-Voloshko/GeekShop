from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from autorisationapp.forms import loginUser, registerUser, ChangeProfil
from django.contrib import messages
from basket.views import Basket

# Create your views here.


def login(request):
    if request.method == "POST":
        form = loginUser(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reversed('mineapp:index'))
    else:
        form = loginUser()
    context = {'form': form}
    return render(request, 'autorisationapp/login.html', context)


def register(request):
    if request.method == "POST":
        form = registerUser(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reversed('autorisationapp:login'))
    else:
        form = registerUser()
    context = {'form': form}
    return render(request, 'autorisationapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reversed("index"))


def profils(request):
    if request.method == 'POST':
        form = ChangeProfil(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reversed('autorisationapp:profil'))
    else:
        form = ChangeProfil(instance=request.user)
        context = {'form': form,
                   'baskets': Basket.objects.filter(user=request.user)
                   }
    return render(request, 'autorisationapp/profil', context)
