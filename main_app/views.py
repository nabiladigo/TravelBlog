from django.shortcuts import render, redirect
from django.views import View 
from django.views.generic.base import TemplateView
from .models import Post

from django.views.generic import  DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
# from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponse


# Create your views here.


class PostList(TemplateView):
   
    template_name = "post.html"
    # using the id to show the new post first
    ordering = ['-public_date' ]

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        name= self.request.GET.get("name")

        if name != None:
            context["posts"] = Post.objects.filter(name_icontains=name)
            context["header"]= f"Searching for {name}"
        else:
            context["posts"] = Post.objects.all()
            context["header"] = "posts"
        return context



class PostDetail(DetailView):
    model= Post
    template_name = "post_detail.html"



class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = "post_update.html"

    def get_success_url(self):
        return reverse( 'post_detail', kwargs={'pk': self.object.pk})
    

class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = "/posts/"


class PostCreate(CreateView):
    model = Post
    fields =['title', 'author', 'body']
    template_name = "post_create.html"

    # def get_succes_url(self):
    #     return redirect('post_detail', kwargs={'pk':self.object.pk})



# class SignUp(View):
#     def get(self, request):
#         form = UserCreationForm()
#         context = {"form": form }
#         return render(request, "registration/signup.html", context)

#     def post(self, request):
#         form = UserCreationForm(request.Post)
#         if form.is_valid():
#             user= form.save()
#             login(request, user)
#             return redirect("profile")
#         else:
#             context = {"form": form}
#             return render(request, "registration/signup.html", context)

