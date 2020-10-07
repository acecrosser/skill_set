# Генератор своих тегов для отображения их в шаблонах
from django import template
from ..models import Post
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


# тег кол-во постов
@register.simple_tag
def total_posts():
    return Post.published.count()


# тег показывает последнии посты
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


# обрабатывает все через markdown
@register.filter(name='markdown') # перемена name будет использоваться как название тега в шаблоне
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.simple_tag()
def function_tools():
    return 'nothing not now'
