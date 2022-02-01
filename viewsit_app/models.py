"""
     Model for the Channel and Channel Posts
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Channel(models.Model):
    """ Channel Model """
    topic = models.CharField(max_length=50)
    topic_url = models.SlugField(max_length=50, unique=True)
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


class ChannelPosts(models.Model):
    """ Channel Posts Model """
    title = models.CharField(max_length=200)
    slug_url = models.SlugField(max_length=250, unique=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE,
                                related_name='channelposts')
    channel_post = models.CharField(max_length=200, blank=True)
    post_image = CloudinaryField('image', blank=True)
    post_url = models.URLField(max_length=250, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="authorposts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
