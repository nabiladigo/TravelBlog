from audioop import reverse
from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from datetime  import datetime, date
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    image = models.CharField(max_length=250)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body= models.TextField()
    public_date= models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title  + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))
