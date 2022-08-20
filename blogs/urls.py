from django.urls import path

from .views import BlogList, BlogDetail, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("blog_list", BlogList.as_view(), name="blog_list"),
    path("<int:pk>", BlogDetail.as_view(), name="blog_detail"),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('<int:pk>/update', BlogUpdateView.as_view(), name='update_blog'),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name='delete_blog'),
]