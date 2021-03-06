from django.views.generic import TemplateView
from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

# django looks for the first one that matches in the list
urlpatterns = [
    path('', views.post_list, name='post_list'), # list is the default page so no path extension
    path('create/', views.post_create, name='post_create'), # with the name attribute, we can just reference the name 
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:id>/edit/', views.post_update, name='post_edit'),
    path('<int:id>/delete/', views.post_delete, name='post_delete'),
]
