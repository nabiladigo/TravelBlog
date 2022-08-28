from django.urls import path
from .import views
from .views import PostLike
urlpatterns =[
    path('', views.Home.as_view(), name="home"),
    path('posts/', views.PostList.as_view(), name="post"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name= "post_update"),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),
    path('posts/new/', views.PostCreate.as_view(), name= "post_create"),
    path('like/<int:pk>/', PostLike, name="post_like"),
    

]