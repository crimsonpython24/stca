from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.urls import reverse
from django.views import generic

from .models import User
from .forms import SignUpForm, UserSettingForm

# Create your views here.
class LoginViewRedirect(auth_views.LoginView):
    def get_success_url(self):
        return reverse('profile', args=[self.request.user.username])


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


def user_settings(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = UserSettingForm()
            user = request.user
            context = { 'user': user, 'form': form }
            return render(request, 'accounts/user_settings.html', context)
        elif request.method == 'POST':
            form = UserSettingForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            context = { 'user': request.user, 'form': form }
            return render(request, 'accounts/user_settings.html', context)
    else:
      return HttpResponse('Unauthorized', status=401)