from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Blog
from django.urls import reverse_lazy

# Create your views here.

class BlogList(ListView):
    template_name = "pages/blog_list.html"
    model = Blog
    context_object_name = "blog_list"


class BlogDetail(DetailView):
    template_name = "pages/blog_detail.html"
    model = Blog
    context_object_name = "camp"

class BlogCreateView(CreateView):
    template_name = 'pages/blog_create.html'
    model = Blog
    fields = ['title', 'description', 'posted_by']


class BlogUpdateView(UpdateView):
    template_name = 'pages/blog_update.html'
    model = Blog
    fields = ['title', 'description', 'posted_by']


class BlogDeleteView(DeleteView):
    template_name = 'pages/blog_delete.html'
    model = Blog
    success_url = reverse_lazy('blog_list')