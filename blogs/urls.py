from django.urls import path

from .views import BlogList, BlogDetail

urlpatterns = [
    path("blog_list", BlogList.as_view(), name="blog_list"),
    path("<int:pk>", BlogDetail.as_view(), name="blog_detail"),
]