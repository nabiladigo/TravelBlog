
from django.shortcuts import render, get_object_or_404
# from django.views import View 
from django.views.generic.base import TemplateView
from .models import Post

from django.views.generic import  DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from django.http import HttpResponseRedirect


# Create your views here.



class PostList(TemplateView):
   
    template_name = "post.html"
    
    # using the id to show the new post first
    ordering = ['-public_date' ]

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        title= self.request.GET.get("title")

        if title != None:
            context["posts"] = Post.objects.filter(name_icontains=title)
            context["header"]= f"Searching for {title}"
        else:
            context["posts"] = Post.objects.all()
            context["header"] = "posts"
        return context



class PostDetail(DetailView):
    model= Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context= super(PostDetail, self).get_context_data( **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True

        context["total_likes"]= total_likes
        context["liked"]= liked


        return  context



class PostUpdate(UpdateView):
    model = Post
    fields = ['image','title', 'author', 'body']
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

    def form_valid(self, form):
        form.instance.user= self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('post_detail', kwargs={'pk': self.object.pk})



def PostLike(request, pk):
    post= get_object_or_404(Post, id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked= True

    # to stay in the same page without the user notice anything
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))






