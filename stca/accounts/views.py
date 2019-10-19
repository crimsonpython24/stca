from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.urls import reverse
from django.views import generic

from .models import User
from .forms import SignUpForm, UserNameForm, UserTextForm, UserAvatarForm

# Create your views here.
class LoginViewRedirect(auth_views.LoginView):
    def get_success_url(self):
        return reverse('profile', args=[self.request.user.username])

    template_name = "registration/login2.html"

class SignupView(generic.CreateView):
    model = User
    form_class = SignUpForm

    def get_success_url(self):
        return reverse('login')


class ProfileView(generic.ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

class TemplateTestView(generic.TemplateView):
    template_name = "temp/login.html"

    
class TemplateTestView2(generic.TemplateView):
    template_name = "temp/login2.html"

def user_settings_name(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = UserNameForm()
            user = request.user
            context = { 'user': user, 'form': form }
            return render(request, 'accounts/user_settings_name.html', context)
        elif request.method == 'POST':
            form = UserNameForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            context = { 'user': request.user, 'form': form }
            return render(request, 'accounts/user_settings_name.html', context)
    else:
      return HttpResponse('Unauthorized', status=401)

class SettingsView(generic.TemplateView):
    model = User
    template_name = 'accounts/user_settings2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

def user_settings_text(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = UserTextForm()
            user = request.user
            context = { 'user': user, 'form': form }
            return render(request, 'accounts/user_settings_text.html', context)
        elif request.method == 'POST':
            form = UserTextForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            context = { 'user': request.user, 'form': form }
            return render(request, 'accounts/user_settings_text.html', context)
    else:
      return HttpResponse('Unauthorized', status=401)

def user_settings_avatar(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = UserAvatarForm()
            user = request.user
            context = { 'user': user, 'form': form }
            return render(request, 'accounts/user_settings2.html', context)
        elif request.method == 'POST':
            form = UserAvatarForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            context = { 'user': request.user, 'form': form }
            return render(request, 'accounts/user_settings_avatar.html', context)
    else:
      return HttpResponse('Unauthorized', status=401)