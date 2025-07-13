from django import template
register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='to')
def to(value, arg):
    return range(value, arg)
