from . import views
from django.urls import path

urlpatterns = [

     path('', views.ChannelList.as_view(), name='home'),
     path('channel_view_all/', views.ChannelViewAll.as_view(), name='channel_view_all'),
     path('channel_list/', views.ChannelList.as_view(), name='channel_list'),
     path('channel_view/<slug>/', views.ChannelView.as_view(), name='channel_view'),
     path('channel_view/', views.ChannelViewAll.as_view(), name='channel_view'),
     path('channel_form/', views.ChannelCreate.as_view(), name='channel_form'),
]
