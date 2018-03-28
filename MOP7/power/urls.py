from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('signup',views.signupview,name='signup'),
    path('login',auth_views.login,{'template_name': 'power/login.html'},name='login'),
    path('logout', auth_views.logout,{'next_page': '/'}, name='logout'),
    path('loggedin',views.logged_in,name='logged_in'),
    path('graph',views.graph,name='graph'),
    path('slider',views.slider,name='slider'),

]