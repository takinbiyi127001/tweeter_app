from django.urls import path


# from .views import TweetCreatView, TweetListView
from . import views

urlpatterns = [
    path('tweets/new/', views.tweet_new, name='tweet_new'),
    path('', views.tweet_list, name='home'),


    # path('', TweetListView.as_view(), name='home'),
    # path('tweets/new/', TweetCreatView.as_view(), name='tweet_new')
]
