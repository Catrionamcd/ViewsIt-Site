from django.shortcuts import render, get_object_or_404, reverse
from django.utils.text import slugify
from django.views import generic, View
from .models import Channel
from cloudinary.forms import cl_init_js_callbacks

class ChannelList(generic.ListView):
    model = Channel
    queryset = Channel.objects.filter(status=1).order_by("-created_on")
    
    template_name = "channel_list.html"
