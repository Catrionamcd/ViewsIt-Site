from django.contrib import admin
from .models import Channel, ChannelPosts

# Admin for Channel and ChannelPosts models


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):

    prepopulated_fields = {'topic_url': ('topic',)}
    list_filter = ('status', 'updated_on')
    list_display = ('topic', 'topic_url', 'status', 'created_on', 'updated_on')
    search_fields = ('topic', 'description')


@admin.register(ChannelPosts)
class ChannelPostsAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug_url': ('title',)}
    list_display = ('title', 'author', 'channel_post', 'updated_on', 'status')
    # list_filter = ('approved', 'created_on')
    # search_fields = ('name', 'email', 'body')
    # actions = ['approve_comments']

    # def approve_comments(self, request, queryset):
    #     queryset.update(approved=True)

# admin.site.register(Channel)
# admin.site.register(ChannelPosts)
