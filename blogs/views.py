from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog

# Create your views here.

class BlogList(ListView):
    template_name = "pages/blog_list.html"
    model = Blog
    context_object_name = "blog_list"


class BlogDetail(DetailView):
    template_name = "pages/blog_detail.html"
    model = Blog
    context_object_name = "camp"