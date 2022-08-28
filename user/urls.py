from django.urls import path
from .import views

urlpatterns =[
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('edit/', views.ProfileEdit.as_view(), name="profile_edit"),
    

]