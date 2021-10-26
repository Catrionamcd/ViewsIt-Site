from .models import Channel
from django import forms


class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ('topic', 'description',)
