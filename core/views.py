
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from .forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth import logout

from json import loads

def update_session(request : HttpRequest):
  if request.method == "POST":
    body = dict(loads(request.body.decode()))
    for k, v in body.items():
      request.session[k] = v
    print(request.session.items())
    return HttpResponse("ok")
  return HttpResponseRedirect("/")


class UserLoginView(LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Register failed!")
  else:
    form = RegistrationForm()

  context = { 'form': form }
  return render(request, 'accounts/register.html', context)

def logout_view(request):
  logout(request)
  return redirect('/')

class UserPasswordResetView(PasswordResetView):
  template_name = 'pages/profiles/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'pages/profiles/password_reset_confirm.html'
  form_class = UserSetPasswordForm
