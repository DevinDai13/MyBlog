from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import urllib.parse
from django.utils import timezone
from django.urls import reverse
from .models import Post
from .forms import PostForm


def post_list(request):
    queryset = Post.objects.all().order_by("-timestamp") # order from most recent to oldest negative timestamp

    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(title__icontains=query)
    paginator = Paginator(queryset, 5) # Show 5 per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    if (request.user.is_authenticated):
        context_data = {
            "post_list":queryset,
            "title":"List"
            "page_request_var"
        }
    else:
        context_data = {
            "title":"Not logged in"
        }

    return render(request, "base.html", context_data)

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser or not request.user.is_authenticated:   # if not a staff or suepruser, unalbe to create post
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user   # assume user is logged in 
        instance.save()
        return HttpResponseRedirect(reverse("post_detail", kwargs={"id":instance.id}))
    
    context_data = {
        "form":form,
    }
    return render(request, "form.html", context_data)

def post_detail(request, id=None): #named paramter
    instance = get_object_or_404(Post, id=id) # this is the query that we used to access the database
    share_string = urllib.parse.quote(instance.content)
    context_data = {
        "title":instance.title,
        "instance":instance,
        "share_string":share_string,
    }
    return render(request, "post_detail.html", context_data)

def post_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:   # if not a staff or suepruser, unalbe to edit post
        raise Http404
    instance = get_object_or_404(Post, id=id) # this is the query that we used to access the database
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
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
    if not request.user.is_staff or not request.user.is_superuser:   # if not a staff or suepruser, unalbe to delete post
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect("post_list")


