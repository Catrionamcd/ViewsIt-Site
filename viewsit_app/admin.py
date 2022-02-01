"""
    Admin for Channel and Channel Post models
"""

from django.contrib import admin
from .models import Channel, ChannelPosts


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    """
        Prepopulate url field for Channel model & set up displays
    """

    prepopulated_fields = {'topic_url': ('topic',)}
    list_filter = ('status', 'updated_on')
    list_display = ('topic', 'topic_url', 'status', 'created_on', 'updated_on')
    search_fields = ('topic', 'status')
    actions = ['channel_publish']

    def channel_publish(self, request, queryset):
        queryset.update(status=1)


@admin.register(ChannelPosts)
class ChannelPostsAdmin(admin.ModelAdmin):
    """
        Prepopulate url field for Channel model & set up displays
    """

    prepopulated_fields = {'slug_url': ('title',)}
    list_display = ('title', 'author', 'channel', 'channel_post', 'updated_on',
                    'status')
    list_filter = ('status', 'author', 'updated_on')
    search_fields = ('title', 'author', 'channel_post')
    actions = ['posts_approve']

    def posts_approve(self, request, queryset):
        queryset.update(status=1)
