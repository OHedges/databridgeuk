from django import template

register = template.Library()

@register.filter(is_safe=True)
def is_num(value):
    try:
        int('{}'.format(value))
    except ValueError:
        return False
    else:
        return True
