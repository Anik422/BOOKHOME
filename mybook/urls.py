from django.urls import path
from mybook import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),

    #path('login/', LoginView.as_view(template_name='registration/login.html'),name='login'),

    
    path('register/', views.register, name='register'),
    path('auther/', views.view_authors, name='view_authors'),
    path('author_books/<int:id>', views.author_books, name="author_books"),
    path('searching/', views.searching, name='searching'),
    path('branche/', views.branch, name='branch'),
    path('branche/<int:area>', views.branches, name='branches'),
    path('despatch/', views.despatch, name='despatch')
]