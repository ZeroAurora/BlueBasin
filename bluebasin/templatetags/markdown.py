from django import template
from django.template.defaultfilters import stringfilter
from markdown_it import MarkdownIt

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def markdown(value: str):
    return MarkdownIt("js-default").render(value)
