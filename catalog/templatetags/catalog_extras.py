from django import template

register = template.Library()

@register.filter(name='prettyprinttags')
def prettyprinttags(value):
    value = str(value).replace('_', ' ')
    value = value[0].upper() + value[1:]
    return value