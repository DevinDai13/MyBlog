from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


# where the images are going to be uploaded to 
# images go to the Eg. images/2/car.jpg the post ID folder
def upload_location(instance, filename):
    return str(instance.id) + "/" + str(filename)

class Post(models.Model):
    title = models.CharField(max_length = 120)
    image = models.ImageField(null=True, blank=True, width_field="width", height_field="height", upload_to=upload_location)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True) #will update and be saved over and over when it gets updated
    timestamp = models.DateTimeField(auto_now_add=True) # saved and set only one time

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
'''
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)  # slugify the title
    if new_slug is not None:        # if a new slug is coming thorugh, then set slug to be new slug
        slug = new_slug              
    qs = Post.objects.filter(slug=slug).order_by("-id")
    if qs.exists():                 # check again
        new_slug = "%s-%s" %(slug, qs.first().id)   # run the new instance one more time
        return create_slug(instance, new_slug=new_slug)
    else:
        return slug

# A "slug" is a way of generating a valid URL, generally using data already obtained.(Eg. slug uses the title of an article to generate a URL.)
# this is only supposed to receive sender and instance but if it receives other arguments, then just put those to args and kwargs and not worry about them
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post) '''
