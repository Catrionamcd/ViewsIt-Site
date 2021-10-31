from . import views
from django.urls import path

urlpatterns = [

     path('', views.ChannelViewAll.as_view(), name=''),
     path('home', views.ChannelViewAll.as_view(), name='home'),
     path('account_register/', views.Register.as_view(), name="account_register"),
     path('user_login/', views.LoginUser.as_view(), name="user_login"),
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
     path('channel_post_approve/<slug>/<post_approval_type>/', views.ChannelPostApprove.as_view(), 
          name='channel_post_approve'),
     path('channel_post_approve/<channel_slug>/<post_slug>/<post_approval_type>/', views.ChannelPostApprove.as_view(), 
          name='channel_post_approve'),
          path('channel_post_edit/<post_slug>/', views.ChannelPostEdit.as_view(), 
          name='channel_post_edit'),
     path('channel_post_edit/<channel_slug>/<post_slug>/<', views.ChannelPostEditWithChannel.as_view(), 
          name='channel_post_edit'),
     path('channel_post_delete/<post_slug>/', views.ChannelPostDelete.as_view(), 
          name='channel_post_delete'),
     path('channel_post_delete/<channel_slug>/<post_slug>/', views.ChannelPostDeleteWithChannel.as_view(), 
          name='channel_post_delete'),

]
