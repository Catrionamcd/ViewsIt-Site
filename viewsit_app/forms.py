from .models import Channel, ChannelPosts
from django import forms


class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ('topic', 'description',)
        labels = {
            'topic': '<strong>Channel Topic:</strong>',
            'description': '<strong>Channel Description:</strong>'
        }


class ChannelPostForm(forms.ModelForm):
    class Meta:
        model = ChannelPosts
        fields = ('title', 'post_image', 'channel_post', 'post_url',)


class ChannelPostFormWithChannel(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ChannelPostFormWithChannel, self).__init__(*args, **kwargs)
        self.fields['channel'].queryset = Channel.objects.filter(status=1)

    class Meta:
        model = ChannelPosts
        fields = ('channel', 'title', 'post_image', 'channel_post', 'post_url',)
