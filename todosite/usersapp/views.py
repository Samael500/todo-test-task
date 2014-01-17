from django.shortcuts import render

from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

def SignUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse('usersapp:signin'))
    else:
        form = UserCreationForm()
    return render(request, 'usersapp/signup.html', {'form': form,})

def SignIn(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('todoapp:index'))
    if request.method == 'POST':
        form = AuthenticationForm(None, request.POST or None)
        nextpage = request.GET.get('next', reverse('todoapp:index'))
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(nextpage)
    else:
        form = AuthenticationForm()
    return render(request, 'usersapp/signin.html', {'form': form,})

def SignOut(request):
    logout(request)
    return render(request, 'usersapp/logout.html')