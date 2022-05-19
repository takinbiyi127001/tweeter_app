from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Tweet


# Create your views here.

class TweetListView(ListView):
    model = Tweet
    template_name = 'tweets/home.html'


class TweetCreatView(CreateView):
    model = Tweet
    template_name = 'tweets/tweet_new.html'
    fields = ['user', 'body']

    def get_success_url(self):
        return reverse('home')
