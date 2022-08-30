from django.shortcuts import render
from django.views import generic, View

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name= "registration/signup.html"
    success_url = reverse_lazy('login')


@login_required
def profile(request):
    return render(request, 'registration/profile.html')

    
class ProfileEdit(generic.CreateView):
    form_class = UserChangeForm
    template_name= "registration/profile_edit.html"
    success_url = reverse_lazy('post')

    def get_object(self):
        return self.request.user



