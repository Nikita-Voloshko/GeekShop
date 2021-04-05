from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from autorisationapp.forms import loginUser, registerUser
from django.contrib import messages

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
