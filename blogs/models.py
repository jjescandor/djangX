from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=64)
    posted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default=" ")
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])