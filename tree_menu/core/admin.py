from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from core.models import main_menu


class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(main_menu, MenuItemMPTTModelAdmin)
