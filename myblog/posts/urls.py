from django.views.generic import TemplateView
from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

# django looks for the first one that matches in the list
urlpatterns = [
    path('', views.post_list, name='post list'), # list is the default page so no path extension
    path('create/', views.post_create, name='post create'),
    path('detail/', views.post_detail, name='post detail'),
    path('update/', views.post_update, name='post update'),
    path('delete/', views.post_delete, name='post delete'),

]
