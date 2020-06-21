from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Post
from .forms import PostForm


def post_list(request):
    queryset = Post.objects.all().order_by("-timestamp") # order from most recent to oldest negative timestamp
    paginator = Paginator(queryset, 5) # Show 5 per page
    page_number = request.GET.get('page')
    post_list = paginator.get_page(page_number)

    if (request.user.is_authenticated):
        context_data = {
            "post_list":queryset,
            "title":"List"
        }
    else:
        context_data = {
            "title":"Not logged in"
        }

    return render(request, "base.html", context_data)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse("post_detail", kwargs={"id":instance.id}))
    
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

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id) # this is the query that we used to access the database
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse("post_detail", kwargs={"id":instance.id}))
    
    context_data = {
        "title":instance.title,
        "instance":instance,
        "form":form,
    }
    return render(request, "form.html", context_data)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect("post_list")


