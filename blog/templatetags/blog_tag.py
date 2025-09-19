from django import template
from blog.models import BlogPost

register = template.Library()

@register.filter(name='snip')
def snip(value,arg):
    return value[:arg]

@register.inclusion_tag('blog/inclusion/popular_posts.html')
def popular_posts():
    posts = BlogPost.objects.all().order_by('view_count')[:4]
    return {'posts': posts}

@register.inclusion_tag('blog/inclusion/last_posts.html')
def last_posts(arg=4):
    posts = BlogPost.objects.all().order_by('-created_on')[:arg]
    return {'posts': posts}


