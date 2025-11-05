from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from .forms                    import UserPasswordChangeForm, EditProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserChangeForm

def display_user(request : HttpRequest):
    user : User = request.user # type: ignore
    form = UserChangeForm(request.POST, instance=user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
    else:
        form = EditProfileForm(instance=request.user)
    
    return render(request, "pages/profiles/profile.html", {
        "segment" : "profile",
        "user" : user,
        "form" : form
    })

def change_password(request : HttpRequest):
    user : User = request.user # type: ignore
    UserPasswordChangeView.extra_context = {
        "segment" : "change_password",
        "user" : user,
    }
    return UserPasswordChangeView.as_view()(request)
    
class UserPasswordChangeView(PasswordChangeView):
  template_name = 'pages/profiles/password_change.html'
  form_class = UserPasswordChangeForm