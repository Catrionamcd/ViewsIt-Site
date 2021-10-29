from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.utils.text import slugify
from django.utils import timezone
from django.views import generic, View
from cloudinary.forms import cl_init_js_callbacks
from .models import Channel, ChannelPosts
from .forms import ChannelForm, ChannelPostForm, ChannelPostFormWithChannel, NewUserForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm


class Register(View):
    model = User

    def get(self, request, *args, **kwargs):
     
        return render(
            request,
            "register.html",
            {
                "new_user_form": NewUserForm()
            },
        )

        # form = NewUserForm(request.POST)

        # if form.is_valid():
        #     user = form.save()
        #     login(request, user)
        #     messages.success(request, "Registration successful.")
        #     return redirect("main:homepage")
        # messages.error(request, "Unsuccessful registration. Invalid information.")
        # form = NewUserForm()


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
            queryset = ChannelPosts.objects.filter(channel=channel).filter(status=1).filter(channel__status__exact=1).order_by("-updated_on")
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

        queryset = ChannelPosts.objects.filter(status=1).filter(channel__status__exact=1).order_by("-updated_on")

        return render(
            request,
            "channel_view.html",
            {
                "post_list": queryset,
            },
        )


class ChannelViewSearch(View):

    def get(self, request, slug, *args, **kwargs):
        search_string = request.GET.get('search_string', '')
        if search_string.isspace():
            search_string = ""
        
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
            queryset = ChannelPosts.objects.filter(
                Q(channel__exact=channel),
                Q(status__exact=1),
                Q(channel__status__exact=1),
                Q(title__icontains=search_string) | Q(channel_post__icontains=search_string)
                ).order_by("-updated_on")
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
                "messages": messages,
                "search_place_holder": search_string
            },
        )


class ChannelViewSearchAll(View):

    def get(self, request, *args, **kwargs):
        search_string = request.GET.get('search_string', '')
        if search_string.isspace():
            search_string = ""

        queryset = ChannelPosts.objects.filter(
            Q(status__exact=1),
            Q(channel__status__exact=1),
            Q(title__icontains=search_string) | Q(channel_post__icontains=search_string)
            ).order_by("-updated_on")

        return render(
            request,
            "channel_view.html",
            {
                "post_list": queryset,
                "search_place_holder": search_string
            },
        )


class ChannelCreate(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/home/')

        return render(
            request,
            "channel_form.html",
            {
                "channelsubmitted": False,
                "channel_form": ChannelForm()
            },
        )

    def post(self, request, *args, **kwargs):
        channelsubmitted = False
        messages = ()
        
        if not request.user.is_authenticated:
            return redirect('/home/')

        channel_form = ChannelForm(data=request.POST)
        if channel_form.is_valid():

            try:
                channel = Channel.objects.get(topic=channel_form.instance.topic)
                channel_form = ChannelForm()
                messages = messages + ("Channel already exists",)
            except Channel.DoesNotExist:
                channel_form.instance.topic_url = slugify(channel_form.instance.topic)
                channel_form.instance.author = request.user
                channel_form.save()
                channelsubmitted = True
        else:
            channel_form = ChannelForm()

        return render(
            request,
            "channel_form.html",
            {
                "channelsubmitted": channelsubmitted,
                "channel_form": channel_form,
                "messages": messages
            },
        )


class ChannelEdit(View):

    def get(self, request, slug, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/home/')

        try:
            channel = Channel.objects.get(topic_url=slug, author=request.user)
        except Channel.DoesNotExist:
            return redirect('/home/') 

        return render(
            request,
            "channel_form.html",
            {
                "channelsubmitted": False,
                "topic": channel.topic,
                "channel_form": ChannelForm(initial={'topic': channel.topic, 'description': channel.description})
            },
        )

    def post(self, request, slug, *args, **kwargs):
        channelsubmitted = False
        messages = ()

        if not request.user.is_authenticated:
            return redirect('/home/')

        channel_form = ChannelForm(data=request.POST)
        if channel_form.is_valid():

            valid_update = False
            try:
                channel = Channel.objects.get(topic_url=slug)
                if channel.author == request.user:
                    if channel.topic == channel_form.instance.topic:
                        valid_update = True
                    else:
                        try:
                            Channel.objects.get(topic=channel_form.instance.topic)
                            # channel_form.instance.topic = channel.topic
                            messages = ("This channel name is already being used",)
                        except Channel.DoesNotExist:
                            valid_update = True
                else:
                    messages = ("You are not the owner of this channel",)               
            except Channel.DoesNotExist:
                messages = ("Channel does not exist",)

            if valid_update:
                channel.topic = channel_form.instance.topic
                channel.topic_url = slugify(channel_form.instance.topic)
                channel.description = channel_form.instance.description
                channel.status = 0
                channel.save()
                channelsubmitted = True

        
        return render(
            request,
            "channel_form.html",
            {
                "channelsubmitted": channelsubmitted,
                "channel_form": channel_form,
                "messages": messages
            },
        )


class ChannelManage(generic.ListView):

    def get(self, request, *args, **kwargs):
        queryset = Channel.objects.filter(author=request.user).order_by("-created_on")


        return render(
            request,
            "channel_manage.html",
            {
                "channel_list": queryset,
            },
        )


class ChannelDelete(View):

    def post(self, request, slug, *args, **kwargs):
        messages = ()
        if not request.user.is_authenticated:
            return redirect('/home/')

        try:
            channel = Channel.objects.get(topic_url=slug, author=request.user)
            channel.delete()
            messages = messages + ("Channel deleted successfully",)
        except Channel.DoesNotExist:
            messages = messages + ("Channel deletion failed",)

        queryset = Channel.objects.filter(author=request.user).order_by("-created_on")

        return render(
            request,
            "channel_manage.html",
            {
                "channel_list": queryset,
                "messages": messages
            },
        )        


class ChannelPost(View):

    def get(self, request, slug, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/home/')

        return render(request, 'channel_post.html',
            {
                "backend_form": ChannelPostForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        messages = ()
        if not request.user.is_authenticated:
            return redirect('/home/')

        try:
            channel = Channel.objects.get(topic_url=slug)
            context = dict(backend_form = ChannelPostForm())

            if channel.status == 0:
                messages = messages + ("Channel not approved: Cannot post to this channel",)
            else:
                form = ChannelPostForm(request.POST, request.FILES)
                if form.is_valid():
                    form.instance.slug_url = slugify(form.instance.title + str(timezone.now()))
                    channel_post = form.save(commit=False)
                    channel_post.author = request.user
                    channel_post.channel = channel
                    channel_post.save()
                    messages = messages + ("Post upload completed, it will need to be approved by the channel owner",)
                    return render(request, 'channel_view.html',
                        {
                            "messages": messages
                        },
                    )
                else:
                    messages = messages + ("Error: Problem with data entered",)
        except Channel.DoesNotExist:
            messages = messages + ("Error posting to this channel",) 

        return render(request, 'channel_post.html',
            {
                "backend_form": ChannelPostForm(),
                "messages": messages
            },
        )

class ChannelPostWithChannel(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/home/')

        return render(request, 'channel_post.html',
            {
                "backend_form": ChannelPostFormWithChannel(),
            },
        )

    def post(self, request, *args, **kwargs):
        messages = ()
        if not request.user.is_authenticated:
            return redirect('/home/')

        context = dict(backend_form = ChannelPostFormWithChannel())

        form = ChannelPostFormWithChannel(request.POST, request.FILES)
        if form.is_valid():
            try:
                channel = Channel.objects.get(id=form.instance.channel.id)
                if channel.status == 0:
                    messages = messages + ("Channel not approved: Cannot post to this channel",)
                else:                      
                    form.instance.slug_url = slugify(form.instance.title + str(timezone.now()))
                    channel_post = form.save(commit=False)
                    channel_post.author = request.user
                    # channel_post.channel = channel
                    channel_post.save()
                    messages = messages + ("Post upload completed, it will need to be approved by the channel owner",)
                    return render(request, 'channel_view.html',
                        {
                            "messages": messages
                        },
                    )
            except Channel.DoesNotExist:
                messages = messages + ("Error: Channel not found",)
        else:
            messages = messages + ("Error: Problem with data entered",)

        return render(request, 'channel_post.html',
            {
                "backend_form": ChannelPostFormWithChannel(),
                "messages": messages
            },
        )
