from django.contrib import admin
from .models import Post

# django model admin documentation 
class PostModelAdmin(admin.ModelAdmin):
    list_display = ("__str__", "timestamp") # for custimizing the dispolay of admin page
    list_filter = ["last_updated", "timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)