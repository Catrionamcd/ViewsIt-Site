from . import views
from django.urls import path

urlpatterns = [

     path('', views.ChannelList.as_view(), name='home'),
     path('acc_signup1/', views.Register.as_view(), name="acc_signup1"),
     path('channel_view_all/', views.ChannelViewAll.as_view(), name='channel_view_all'),
     path('channel_list/', views.ChannelList.as_view(), name='channel_list'),
     path('channel_view/<slug>/', views.ChannelView.as_view(), name='channel_view'),
     path('channel_view/', views.ChannelViewAll.as_view(), name='channel_view'),
     path('channel_view_search/<slug>', views.ChannelViewSearch.as_view(), name='channel_view_search'),
     path('channel_view_search/', views.ChannelViewSearchAll.as_view(), name='channel_view_search'),
     path('channel_form/', views.ChannelCreate.as_view(), name='channel_form'),
     path('channel_form/<slug>/', views.ChannelEdit.as_view(), name='channel_form'),
     path('channel_post/<slug>/', views.ChannelPost.as_view(), name='channel_post'),
     path('channel_post/', views.ChannelPostWithChannel.as_view(), name='channel_post'),
     path('channel_manage/', views.ChannelManage.as_view(), name='channel_manage'),
     path('channel_delete/<slug>/', views.ChannelDelete.as_view(),
          name='channel_delete'),

]
