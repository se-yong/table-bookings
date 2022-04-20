from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from ..forms import RegisterForm, LoginForm
from ..models import UserProfile
from django.views.generic import FormView
from django.views import View


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        nickname = form.cleaned_data['nickname']
        profile_image = form.cleaned_data['profile_image']

        user = User.objects.create_user(email, email, password)
        UserProfile.objcets.create(user=user, nickname=nickname, profile_image=profile_image)

        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')
    form_class = LoginForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(self.request, user)
            return super().form_valid(form)
        else:
            messages.warning(self.request, '계정 혹은 비밀번호를 확인해주세요.')
            return redirect(reverse('login'))


class LogoutView(View):

    def get(self, request):
        auth.logout(request)
        return redirect(reverse('index'))