from django import template
from core.models import main_menu

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context):
    menu_items = main_menu.objects.filter(level=1)
    return {
        "menu_items": menu_items,
    }


