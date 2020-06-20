from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

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
    form = PostForm(request.POST or None)
    #if (request.method == 'POST'):
    #    print(request.POST.get("title"))
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    
    context_data = {
        "form":form,
    }
    return render(request, "form.html", context_data)

def post_detail(request, id=None): #named paramter
    instance = get_object_or_404(Post, id=id) # this is the query that we used to access the database
    context_data = {
        "title":instance.title,
        "instance":instance
    }
    return render(request, "post_detail.html", context_data)

def post_update(request):
    return HttpResponse("<h1>update</h1>")

def post_delete(request):
    return HttpResponse("<h1>delete</h1>")

