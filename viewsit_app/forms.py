''' Forms for Registrations, New Channels & Channels Posts '''
from django.contrib.auth.models import User
from django import forms
from django.forms import Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Channel, ChannelPosts


class NewUserForm(UserCreationForm):
    ''' Registraion Form for a New User to the site '''

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    ''' A login form for a user of the site '''

    class Meta:
        model = User
        fields = ('username', 'password')


class ChannelForm(forms.ModelForm):
    ''' A form to set up a new channel '''

    class Meta:
        model = Channel
        fields = ('topic', 'description',)
        labels = {
            'topic': '<strong>Channel Topic:</strong>',
            'description': '<strong>Channel Description:</strong>'
        }

        widgets = {
            'description': Textarea(attrs={'cols': 200, 'rows': 4})
        }


class ChannelPostForm(forms.ModelForm):
    ''' A form to attach a post to a channel '''

    class Meta:
        model = ChannelPosts
        fields = ('title', 'post_image', 'channel_post', 'post_url',)
        labels = {
            'title': '<strong>Post Title:</strong>',
            'post_image': '<strong>Post Image:</strong>',
            'channel_post': '<strong>Post Text:</strong>',
            'post_url': '<strong>Post URL:</strong>'
        }

        widgets = {
            'channel_post': Textarea(attrs={'cols': 200, 'rows': 4})
        }


class ChannelPostFormWithChannel(forms.ModelForm):
    '''
        A form to attach a post to a channel. The
        channel is selected from a drop down menu of
        approved channels.
    '''

    def __init__(self, *args, **kwargs):
        super(ChannelPostFormWithChannel, self).__init__(*args, **kwargs)
        self.fields['channel'].queryset = Channel.objects.filter(status=1)

    class Meta:
        model = ChannelPosts
        fields = ('channel', 'title', 'post_image',
                  'channel_post', 'post_url',)
        labels = {
            'channel': '<strong>Channel:</strong>',
            'title': '<strong>Post Title:</strong>',
            'post_image': '<strong>Post Image:</strong>',
            'channel_post': '<strong>Post Text:</strong>',
            'post_url': '<strong>Post URL:</strong>'
        }

        widgets = {
            'channel_post': Textarea(attrs={'cols': 200, 'rows': 4})
        }
