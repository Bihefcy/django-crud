from django.shortcuts import render
from django.views.generic.edit import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from blog import Post
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DetailView
from django.views.generic.edit import DeleteView



class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['all']
    success_url  = reverse_lazy['blog:all']

class PostUpdateView(UpdateView):
    model = Post
    fields = ['all']
    success_url  = reverse_lazy['blog:all']

class PostDetailView(DetailView):
    model = Post

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:all')
