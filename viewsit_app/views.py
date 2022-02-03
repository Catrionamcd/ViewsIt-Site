"""
   Functions to controls all channel views, updates,deletes and posts
"""
from django.shortcuts import render, reverse, redirect
from django.utils.text import slugify
from django.utils import timezone
from django.views import generic, View
from .models import Channel, ChannelPosts
from .forms import ChannelForm, ChannelPostForm, ChannelPostFormWithChannel
from .forms import NewUserForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q, Count


class Register(View):
    """ Registration for ViewsIt site """

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "register.html",
            {
              "new_user_form": NewUserForm()
            },
        )

    def post(self, request, *args, **kwargs):

        messages = ()

        new_user_form = NewUserForm(data=request.POST)

        if new_user_form.is_valid():
            new_user_form.save()
            return redirect(reverse('home') + "?messages=Registration"
                            " successful")
        messages = ("Unsuccessful registration. Invalid information.",)
        new_user_form = NewUserForm()

        return render(
            request,
            "register.html",
            {
              "messages": messages,
              "new_user_form": NewUserForm()
            },
        )


class LoginUser(View):
    """ User Login """

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "login_user.html",
            {
             "login_user_form": LoginUserForm()
            },
        )

    def post(self, request, *args, **kwargs):

        login_user_form = LoginUserForm(data=request.POST)
        if login_user_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse
                                ('channel_view')+"?messages=Login successful")

        messages = ("Unsuccessful Login. Invalid information.",)

        return render(
            request,
            "login_user.html",
            {
                "messages": messages,
                "login_user_form": LoginUserForm()
            },
        )


class LogoutUser(View):
    """ User Logout """

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "logout_user.html",
            {
                "user_name": request.user.username
            },
        )

    def post(self, request, *args, **kwargs):

        logout(request)
        return redirect(reverse('channel_view')+"?messages=Logout successful")


class ChannelList(generic.ListView):
    """ List Approved Channels """
    model = Channel
    queryset = Channel.objects.filter(status=1).order_by("-created_on")

    template_name = "channel_list.html"


class ChannelView(View):
    """ View the posts of a channel """

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

            if request.user.is_authenticated:
                queryset = ChannelPosts.objects.filter(
                    Q(channel__exact=channel),
                    Q(status__exact=1) |
                    Q(author__exact=request.user) |
                    Q(channel__author__exact=request.user),
                    Q(channel__status__exact=1),
                    ).order_by("-updated_on")
            else:
                queryset = ChannelPosts.objects.filter(
                    Q(channel__exact=channel),
                    Q(status__exact=1),
                    Q(channel__status__exact=1),
                    ).order_by("-updated_on")

        except Channel.DoesNotExist:
            messages = messages + (
                str("Error: Channel " + slug + " does not exist"),)

        return render(
            request,
            "channel_view.html",
            {
                "channel_topic": channel_topic,
                "channel_topic_url": channel_topic_url,
                "channel_description": channel_description,
                "post_list": queryset,
                "messages": messages,
                "current_user": request.user
            },
        )


class ChannelViewAll(View):
    """ View All Channel and all Posts """

    def get(self, request, *args, **kwargs):
        messages = ()

        message_string = request.GET.get('messages', '')
        if message_string:
            messages = messages + (message_string, )

        if request.user.is_authenticated:
            queryset = ChannelPosts.objects.filter(
                Q(status__exact=1) |
                Q(author__exact=request.user) |
                Q(channel__author__exact=request.user),
                Q(channel__status__exact=1),
                ).order_by("-updated_on")
        else:
            queryset = ChannelPosts.objects.filter(
                Q(status__exact=1),
                Q(channel__status__exact=1),
                ).order_by("-updated_on")

        return render(
            request,
            "channel_view.html",
            {
                "post_list": queryset,
                "messages": messages,
                "current_user": request.user
            },
        )


class ChannelViewSearch(View):
    """
         Searches can be made by channel topic, post or user/author
        when a user is wihtin a channel
    """

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

            if request.user.is_authenticated:
                queryset = ChannelPosts.objects.filter(
                    Q(channel__exact=channel),
                    Q(status__exact=1) | Q(author__exact=request.user),
                    Q(channel__status__exact=1),
                    Q(title__icontains=search_string) |
                    Q(channel_post__icontains=search_string) |
                    Q(author__username__icontains=search_string)
                    ).order_by("-updated_on")
            else:
                queryset = ChannelPosts.objects.filter(
                    Q(channel__exact=channel),
                    Q(status__exact=1),
                    Q(channel__status__exact=1),
                    Q(title__icontains=search_string) |
                    Q(channel_post__icontains=search_string) |
                    Q(author__username__icontains=search_string)
                    ).order_by("-updated_on")

        except Channel.DoesNotExist:
            messages = messages + (
                str("Error: Channel " + slug + " does not exist"),)

        return render(
            request,
            "channel_view.html",
            {
                "channel_topic": channel_topic,
                "channel_topic_url": channel_topic_url,
                "channel_description": channel_description,
                "post_list": queryset,
                "messages": messages,
                "search_place_holder": search_string,
                "current_user": request.user
            },
        )


class ChannelViewSearchAll(View):
    """
        Searches can be made by channel topic, post, or user/author
    """

    def get(self, request, *args, **kwargs):
        search_string = request.GET.get('search_string', '')
        if search_string.isspace():
            search_string = ""

        if request.user.is_authenticated:
            queryset = ChannelPosts.objects.filter(
                Q(status__exact=1) | Q(author__exact=request.user),
                Q(channel__status__exact=1),
                Q(title__icontains=search_string) |
                Q(channel_post__icontains=search_string) |
                Q(author__username__icontains=search_string)
                ).order_by("-updated_on")
        else:
            queryset = ChannelPosts.objects.filter(
                Q(status__exact=1),
                Q(channel__status__exact=1),
                Q(title__icontains=search_string) |
                Q(channel_post__icontains=search_string) |
                Q(author__username__icontains=search_string)
                ).order_by("-updated_on")

        return render(
            request,
            "channel_view.html",
            {
                "post_list": queryset,
                "search_place_holder": search_string,
                "current_user": request.user
            },
        )


class ChannelCreate(View):
    """
        Create a new channel. Only registered user can do this.
    """

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

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
            return redirect('home')

        channel_form = ChannelForm(data=request.POST)
        if channel_form.is_valid():

            try:
                Channel.objects.get(topic=channel_form.instance.topic)
                channel_form = ChannelForm()
                messages = messages + ("Channel already exists",)
            except Channel.DoesNotExist:
                channel_form.instance.topic_url = \
                    slugify(channel_form.instance.topic)
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
    """
        Edit a Channel. Only the owner of the channel can do this. If
        a channel is edited, it has to be re-approved by the super user
    """
    def get(self, request, slug, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        try:
            channel = Channel.objects.get(topic_url=slug, author=request.user)
        except Channel.DoesNotExist:
            return redirect('home')

        return render(
            request,
            "channel_form.html",
            {
                "channelsubmitted": False,
                "topic": channel.topic,
                "channel_form": ChannelForm(
                    initial={'topic': channel.topic,
                             'description': channel.description}
                )
            },
        )

    def post(self, request, slug, *args, **kwargs):
        channelsubmitted = False
        messages = ()

        if not request.user.is_authenticated:
            return redirect('home')

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
                            Channel.objects.get(
                                topic=channel_form.instance.topic)
                            messages = ("This channel name is"
                                        " already being used",)
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
    """
        Channel manage will show the number of posts to
        be approved. The channel owner can delete the channel
        and also unapprove posts
    """

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        num_unapproved = Count('channelposts',
                               filter=Q(channelposts__status__lte=0))
        queryset = Channel.objects.filter(author=request.user).order_by(
            "-created_on").annotate(num_unapproved=num_unapproved).annotate(
                posts_count=Count('channelposts'))

        return render(
            request,
            "channel_manage.html",
            {
                "channel_list": queryset,
            },
        )


class ChannelDelete(View):
    """
        Channel Delete. Once a channel is deleted all the posts
        associated with the channel will be deleted
    """

    def post(self, request, slug, *args, **kwargs):
        messages = ()
        if not request.user.is_authenticated:
            return redirect('home')

        try:
            channel = Channel.objects.get(topic_url=slug, author=request.user)
            channel.delete()
            messages = messages + ("Channel deleted successfully",)
        except Channel.DoesNotExist:
            messages = messages + ("Channel deletion failed",)

        queryset = Channel.objects.filter(author=request.user).order_by(
            "-created_on")

        return render(
            request,
            "channel_manage.html",
            {
                "channel_list": queryset,
                "messages": messages
            },
        )


class ChannelPost(View):
    """
        Attach a post to a channel. An image and a link can be attached
        or just a post decsription along with post title
    """

    def get(self, request, slug, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        channel = Channel.objects.get(topic_url=slug)

        return render(request, 'channel_post.html',
                      {
                        "backend_form": ChannelPostForm(),
                        "channel_topic_url": slug,
                        "channel_topic": channel.topic
                       },
                      )

    def post(self, request, slug, *args, **kwargs):
        messages = ()
        if not request.user.is_authenticated:
            return redirect('home')

        try:
            channel = Channel.objects.get(topic_url=slug)

            if channel.status == 0:
                messages = messages
                + ("Channel not approved: Cannot post to this channel",)
            else:
                form = ChannelPostForm(request.POST, request.FILES)
                if form.is_valid():
                    form.instance.slug_url = slugify(
                        form.instance.title + str(timezone.now()))
                    channel_post = form.save(commit=False)
                    channel_post.author = request.user
                    channel_post.channel = channel
                    channel_post.save()
                    messages = messages + ("Post upload completed, it will "
                                           "need to be approved by the channel"
                                           " owner",)

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
                        "messages": messages,
                        "channel_topic": slug
                       },
                      )


class ChannelPostWithChannel(View):
    """
        Attach a post to a channel. The channel can be selected from a
        list of channel in a drop down menu. An image and a link can be
        attached or just a post decsription
    """

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        return render(request, 'channel_post.html',
                      {
                        "backend_form": ChannelPostFormWithChannel(),
                       },
                      )

    def post(self, request, *args, **kwargs):
        messages = ()
        if not request.user.is_authenticated:
            return redirect('home')

        form = ChannelPostFormWithChannel(request.POST, request.FILES)
        if form.is_valid():
            try:
                channel = Channel.objects.get(id=form.instance.channel.id)
                if channel.status == 0:
                    messages = messages + ("Channel not approved: Cannot"
                                           " post to this channel",)
                else:
                    form.instance.slug_url = slugify(
                        form.instance.title + str(timezone.now()))
                    channel_post = form.save(commit=False)
                    channel_post.author = request.user
                    channel_post.save()
                    return redirect(reverse('channel_view')+"?messages=Post"
                                    " upload completed, it will need to be"
                                    " approved by the channel owner")
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


class ChannelPostApprove(View):
    """
        Approve a channel post. Only the author of the channel can do this
    """

    def get(self, request, slug, post_approval_type, *args, **kwargs):
        messages = ()
        channel_topic = ""
        channel_topic_url = ""
        channel_description = ""
        queryset = ""
        approval_type = ""

        if not request.user.is_authenticated:
            return redirect('home')

        try:
            channel = Channel.objects.get(topic_url=slug)
            if channel.author == request.user:
                channel_topic = channel.topic
                channel_topic_url = channel.topic_url
                channel_description = channel.description
                if post_approval_type == "Approve":
                    queryset = ChannelPosts.objects.filter(
                        channel=channel).filter(status=0).order_by(
                            "-updated_on")
                else:
                    queryset = ChannelPosts.objects.filter(
                        channel=channel).filter(status=1).order_by(
                            "-updated_on")
                approval_type = post_approval_type
            else:
                messages = messages
                + ("You are not the channel owner for this channel",)
        except Channel.DoesNotExist:
            messages = messages
            + (str("Error: Channel " + slug + " does not exist"),)

        return render(
            request,
            "channel_view.html",
            {
                "channel_topic": channel_topic,
                "channel_topic_url": channel_topic_url,
                "channel_description": channel_description,
                "post_list": queryset,
                "messages": messages,
                "approval_type": approval_type
            },
        )

    def post(self, request, channel_slug, post_slug, post_approval_type,
             *args, **kwargs):
        messages = ()
        channel_topic = ""
        channel_topic_url = ""
        channel_description = ""
        queryset = ""
        approval_type = ""

        if not request.user.is_authenticated:
            return redirect('home')

        try:
            channel = Channel.objects.get(topic_url=channel_slug)
            if channel.author == request.user:
                channel_topic = channel.topic
                channel_topic_url = channel.topic_url
                channel_description = channel.description
                approval_type = post_approval_type
                try:
                    channel_post = ChannelPosts.objects.get(slug_url=post_slug)
                    if post_approval_type == "Approve":
                        if channel_post.status == 0:
                            channel_post.status = 1
                            channel_post.save()
                        else:
                            messages = messages
                            + ("Error: The post is already approved",)
                        queryset = ChannelPosts.objects.filter(
                            channel=channel).filter(status=0).order_by(
                                "-updated_on")
                    else:
                        if channel_post.status == 1:
                            channel_post.status = 0
                            channel_post.save()
                        else:
                            messages = messages + ("Error: The post is already"
                                                   " in unapproved status",)
                        queryset = ChannelPosts.objects.filter(
                            channel=channel).filter(status=1).order_by(
                                "-updated_on")
                except ChannelPosts:
                    messages = messages
                    + ("Error: The post could not be retrieved for update",)
            else:
                messages = messages
                + ("You are not the channel owner for this channel",)
        except Channel.DoesNotExist:
            messages = messages
            + (str("Error: Channel " + channel_slug + " does not exist"),)

        return render(
            request,
            "channel_view.html",
            {
                "channel_topic": channel_topic,
                "channel_topic_url": channel_topic_url,
                "channel_description": channel_description,
                "post_list": queryset,
                "messages": messages,
                "approval_type": approval_type
            },
        )


class ChannelPostEdit(View):
    """
        Edit a channel post.
    """

    def get(self, request, post_slug, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        try:
            channel_post = ChannelPosts.objects.get(slug_url=post_slug,
                                                    author=request.user)
        except Channel.DoesNotExist:
            return redirect('home')

        return render(request, 'channel_post.html', {
            "backend_form": ChannelPostFormWithChannel(
                initial={'channel': channel_post.channel,
                         'title': channel_post.title,
                         'post_image': channel_post.post_image,
                         'channel_post': channel_post.channel_post,
                         'post_url': channel_post.post_url}),
            },
        )

    def post(self, request, post_slug, *args, **kwargs):
        messages = ()
        if not request.user.is_authenticated:
            return redirect('home')

        try:
            channel_post = ChannelPosts.objects.get(slug_url=post_slug)
            if channel_post.author == request.user:
                form = ChannelPostFormWithChannel(request.POST, request.FILES)
                if form.is_valid():
                    channel_post.channel = form.instance.channel
                    channel_post.title = form.instance.title
                    channel_post.slug_url = slugify(
                        form.instance.title + str(timezone.now()))
                    if form.instance.post_image:
                        channel_post.post_image = form.instance.post_image
                    channel_post.channel_post = form.instance.channel_post
                    channel_post.post_url = form.instance.post_url
                    channel_post.status = 0
                    channel_post.save()
                    return redirect(reverse('channel_view')+"?messages=Post "
                                    "update completed, it will need to be "
                                    "approved by the channel owner")
                else:
                    messages = messages + ("Error: Problem with data entered",)
            else:
                messages = messages
                + ("Cannot update post, you are not the owner",)
        except ChannelPosts.DoesNotExist:
            messages = messages
            + ("Error: Post could not be located for update",)

        return render(request, 'channel_post.html', {
            "backend_form": ChannelPostFormWithChannel(
                initial={'channel': form.instance.channel,
                         'title': form.instance.title,
                         'post_image': form.instance.post_image,
                         'channel_post': form.instance.channel_post,
                         'post_url': form.instance.post_url}),
            "messages": messages
            },
        )


class ChannelPostEditWithChannel(View):
    """
        Edit a channel post with in a channel
    """

    def get(self, request, channel_slug, post_slug, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        try:
            channel_post = ChannelPosts.objects.get(
                slug_url=post_slug, author=request.user)
        except Channel.DoesNotExist:
            return redirect('home')

        return render(request, 'channel_post.html', {
            "backend_form": ChannelPostFormWithChannel(
                initial={'channel': channel_post.channel,
                         'title': channel_post.title,
                         'post_image': channel_post.post_image,
                         'channel_post': channel_post.channel_post,
                         'post_url': channel_post.post_url}),
            },
        )

    def post(self, request, channel_slug, post_slug, *args, **kwargs):
        messages = ()
        slug = channel_slug
        if not request.user.is_authenticated:
            return redirect('home')

        try:
            channel_post = ChannelPosts.objects.get(slug_url=post_slug)
            if channel_post.author == request.user:
                form = ChannelPostFormWithChannel(request.POST, request.FILES)
                if form.is_valid():
                    channel_post.channel = form.instance.channel
                    channel_post.title = form.instance.title
                    channel_post.slug_url = slugify(
                        form.instance.title + str(timezone.now()))
                    if form.instance.post_image:
                        channel_post.post_image = form.instance.post_image
                    channel_post.channel_post = form.instance.channel_post
                    channel_post.post_url = form.instance.post_url
                    channel_post.status = 0
                    channel_post.save()
                    return redirect(reverse('channel_view')+slug+"?messages="
                                    "Post update completed, it will need to be"
                                    " approved by the channel owner")
                else:
                    messages = messages + ("Error: Problem with data entered",)
            else:
                messages = messages
                + ("Cannot update post, you are not the owner",)
        except ChannelPosts.DoesNotExist:
            messages = messages + ("Error: Post could not be "
                                   " located for update",)

        return render(request, 'channel_post.html', {
            "backend_form": ChannelPostFormWithChannel(
                initial={'channel': form.instance.channel,
                         'title': form.instance.title,
                         'post_image': form.instance.post_image,
                         'channel_post': form.instance.channel_post,
                         'post_url': form.instance.post_url}),
            "messages": messages
            },
        )


class ChannelPostDelete(View):
    """
        Delete a channel post
    """

    def post(self, request, post_slug, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('home')
        try:
            channel_post = ChannelPosts.objects.get(slug_url=post_slug)
            if channel_post.author == request.user:
                channel_post.delete()
                return redirect(reverse('channel_view')+"?messages=Post"
                                " successfully deleted")
            else:
                return redirect(reverse('channel_view')+"?messages=Cannot"
                                " Delete: You are not the person who created"
                                " this post")
        except ChannelPosts.DoesNotExist:
            return redirect(reverse('channel_view')+"?messages=Error: Post"
                            " could not be located for deletion")

        return redirect(reverse('channel_view'))


class ChannelPostDeleteWithChannel(View):
    """
        Delete a channel post
    """

    def post(self, request, channel_slug, post_slug, *args, **kwargs):

        slug = channel_slug

        if not request.user.is_authenticated:
            return redirect('home')
        try:
            channel_post = ChannelPosts.objects.get(slug_url=post_slug)
            if channel_post.author == request.user:
                channel_post.delete()
                return redirect(reverse('channel_view')+"?messages=Post"
                                " successfully deleted")
            else:
                return redirect(reverse('channel_view')+slug+"?messages=Cannot"
                                " Delete: You are not the person who created"
                                " this post")
        except ChannelPosts.DoesNotExist:
            return redirect(reverse('channel_view')+slug+"?messages=Error:"
                            " Post could not be located for deletion")

        return redirect(reverse('channel_view')+slug)


class ChannelPostLike(View):
    """
        To like a channel post
    """

    def post(self, request, post_slug, *args, **kwargs):
        messages = ()
        if not request.user.is_authenticated:
            return redirect('home')

        try:
            channel_post = ChannelPosts.objects.get(slug_url=post_slug)
            if channel_post.likes.filter(id=request.user.id).exists():
                channel_post.likes.remove(request.user)
            else:
                channel_post.likes.add(request.user)

            return redirect(reverse('channel_view'))

        except ChannelPosts.DoesNotExist():
            messages = messages + ("Error: Could not locate post",)

        return render(request, 'channel_view.html',
                      {
                        "messages": messages,
                        "current_user": request.user
                      },
                      )


class ChannelPostLikeWithChannel(View):
    """
        To like a channel post
    """

    def post(self, request, channel_slug, post_slug, *args, **kwargs):
        messages = ()
        if not request.user.is_authenticated:
            return redirect('home')
        try:
            channel_post = ChannelPosts.objects.get(slug_url=post_slug)
            if channel_post.likes.filter(id=request.user.id).exists():
                channel_post.likes.remove(request.user)
            else:
                channel_post.likes.add(request.user)

            return redirect(reverse('channel_view')+channel_slug)

        except ChannelPosts.DoesNotExist():
            messages = messages + ("Error: Could not locate post",)

        return render(request, 'channel_view.html',
                      {
                        "messages": messages,
                        "current_user": request.user
                       },
                      )
