
from django import template

register = template.Library()

@register.simple_tag()
def check_if_tree_prefix(path : str) -> bool:
    return path.startswith("/tree/")
