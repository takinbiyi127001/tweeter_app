from django.urls import path


from .views import TweetCreatView, TweetListView


urlpatterns = [
    path('', TweetListView.as_view(), name='home'),
    path('tweets/new/', TweetCreatView.as_view(), name='tweet_new')
]
