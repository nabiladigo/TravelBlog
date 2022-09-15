from django.shortcuts import render
from django.views import generic, View

from .models import Profile

from django.views.generic import  DetailView
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



class ProfilePage(DetailView):
    model = Profile
    template_name = "profile.html"
    def get_context_data(self, **kwargs):
        context = super(ProfilePage, self).get_context_data(**kwargs)
        # context['guide'] = Guide.objects.filter(user=self.request.user)
        return context