from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 120)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True) #will update and be saved over and over when it gets updated
    timestamp = models.DateTimeField(auto_now_add=True) # saved and set only one time

    def __str__(self):
        return self.title