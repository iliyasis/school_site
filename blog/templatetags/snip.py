from django import template

register = template.Library()

@register.filter(name='snip')
def snip(value,arg):
    return value[:arg]