from django.urls import path


from .views import TweetCreatView, TweetListView, SearchView
from . import views

urlpatterns = [
    # path('tweets/new/', views.tweet_new, name='tweet_new'),
    # path('', views.tweet_list, name='home'),

    path('', TweetListView.as_view(), name='home'),
    path('tweets/new/', TweetCreatView.as_view(), name='tweet_new'),
    path('search/', SearchView.as_view(), name='search'),
    path('delete/<int:id>', views.delete, name='delete'),
]
