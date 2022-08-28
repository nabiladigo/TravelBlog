from django.urls import path
from .import views
from .views import profile

urlpatterns =[
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('profile/', profile, name="progile"),
    path('edit/', views.ProfileEdit.as_view(), name="profile_edit"),
    

]