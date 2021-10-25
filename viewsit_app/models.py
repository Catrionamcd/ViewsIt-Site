from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Channel Model

STATUS = ((0, "Draft"), (1, "Published"))

class Channel(models.Model):
    topic = models.CharField(max_length=50)
    topic_url = models.SlugField(max_length=50, unique=True, null=True)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name="channels")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.topic
