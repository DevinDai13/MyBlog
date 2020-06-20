from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse
from .models import Post

def post_list(request):
    queryset = Post.objects.all()
    if (request.user.is_authenticated):
        context_data = {
            "post_list":queryset,
            "title":"List"
        }
    else:
        context_data = {
            "title":"Not logged in"
        }
    return render(request, "index.html", context_data)
    #return HttpResponse("<h1>Main</h1>")

def post_create(request):
    return HttpResponse("<h1>create</h1>")

def post_detail(request):
    instance = get_object_or_404(Post, id=1) # this is the query that we used to access the database
    context_data = {
        "title":instance.title,
        "instance":instance
    }
    return render(request, "post_detail.html", context_data)

def post_update(request):
    return HttpResponse("<h1>update</h1>")

def post_delete(request):
    return HttpResponse("<h1>delete</h1>")

