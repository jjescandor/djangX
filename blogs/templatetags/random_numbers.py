import random
from django import template
from ..models import Blog
register = template.Library()


@register.simple_tag
def random_int():
    c = Blog.objects.all().count()
    return random.randint(1, c)


