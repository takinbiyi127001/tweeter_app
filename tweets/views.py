from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Tweet
# from .forms import TweetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


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


def delete(request, id):
    member = Tweet.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('home'))


class SearchView(ListView):
    model = Tweet
    template_name = 'tweets/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            tweet_result = Tweet.objects.filter(body__contains=query)
            result = tweet_result
        else:
            result = Tweet.objects.all()
        return result


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
