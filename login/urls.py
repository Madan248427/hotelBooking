from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking',views.booking,name='booking'),
    path('login.html',views.login25,name="login"),
    path('signup.html',views.SignupPage,name="signup"),
    path('index.html',views.index,name="home"),
    path('logout',views.logoutuser,name="logout"),
    path('edit<int:id>',views.edit,name='edit'),
    path('delete<int:id>',views.delete,name='delete')
]

