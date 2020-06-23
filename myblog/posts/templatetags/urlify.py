import urllib.parse
from django import template

register = template.Library()

@register.filter  # usign django template and regiter it as something we can use inside the template
def urlify(value):
    return urllib.parse.quote(value)