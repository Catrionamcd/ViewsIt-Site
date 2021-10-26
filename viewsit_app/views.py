from django.shortcuts import render, get_object_or_404, reverse
from django.utils.text import slugify
from django.views import generic, View
from .models import Channel, ChannelPosts
from cloudinary.forms import cl_init_js_callbacks


class ChannelList(generic.ListView):
    model = Channel
    queryset = Channel.objects.filter(status=1).order_by("-created_on")
    
    template_name = "channel_list.html"


class ChannelView(View):

    def get(self, request, slug, *args, **kwargs):
        messages = ()
        channel_topic = ""
        channel_topic_url = ""
        channel_description = ""
        queryset = ""
        try:
            channel = Channel.objects.get(topic_url=slug)
            channel_topic = channel.topic
            channel_topic_url = channel.topic_url
            channel_description = channel.description
            queryset = ChannelPosts.objects.filter(channel=channel).filter(status=1).order_by("-updated_on")
        except Channel.DoesNotExist:
            messages = messages + (str("Error: Channel " + slug + " does not exist"),)        

        return render(
            request,
            "channel_view.html",
            {
                "channel_topic": channel_topic,
                "channel_topic_url": channel_topic_url,
                "channel_description": channel_description,
                "post_list": queryset,
                "messages": messages
            },
        )


class ChannelViewAll(View):

    def get(self, request, *args, **kwargs):

        queryset = ChannelPosts.objects.filter(status=1).order_by("-updated_on")

        return render(
            request,
            "channel_view.html",
            {
                "post_list": queryset,
            },
        )