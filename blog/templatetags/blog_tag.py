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
