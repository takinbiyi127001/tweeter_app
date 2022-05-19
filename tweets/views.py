# from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Tweet
# from .forms import TweetForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# Class-based View
class TweetListView(ListView):
    model = Tweet
    template_name = 'tweets/home.html'


class TweetCreatView(LoginRequiredMixin, CreateView):
    model = Tweet
    template_name = 'tweets/tweet_new.html'
    # fields = ['user', 'body']
    fields = ['body']

    def get_success_url(self):
        return reverse('home')

    def get_login_url(self):
        return reverse('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Function-based View

# def tweet_list(request):
#     context = {
#         'object_list': Tweet.objects.all()
#     }
#     return render(request, 'tweets/home.html', context)
#
#
# def tweet_new(request):
#     if request.method == 'POST':
#         form = TweetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = TweetForm
#
#     return render(request, 'tweets/tweet_new.html', {'form': form})
