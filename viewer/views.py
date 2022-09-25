from logging import getLogger

from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from viewer.forms import MovieForm
from viewer.models import Movie
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
LOGGER = getLogger()


def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie


# class MovieDetailView(LoginRequiredMixin, DetailView):
#   template_name = 'movie_detail.html'
#   model = Movie

class MovieCreateView(LoginRequiredMixin, CreateView):
  template_name = 'form.html'
  form_class = MovieForm
  success_url = reverse_lazy('index')
class MovieUpdateView(LoginRequiredMixin, UpdateView):
  template_name = 'form.html'
  model = Movie
  form_class = MovieForm
  success_url = reverse_lazy('viewer:movies')
class MovieDeleteView(LoginRequiredMixin, DeleteView):
  template_name = 'movie_confirm_delete.html'
  model = Movie
  success_url = reverse_lazy('viewer:movies')

class SubmittableLoginView(LoginView):
  template_name = 'form.html'

class SubmittableLogoutView(LogoutView):
    LOGOUT_REDIRECT_URL='index'
class SubmittablePasswordChangeView(PasswordChangeView):
  template_name = 'form.html'
  success_url = reverse_lazy('index')