from django.contrib import admin
from .models import SideBarItems, OnePageContent, MultiPageContent


class SideBarAdmin(admin.ModelAdmin):
    pass


class OnePageContentAdmin(admin.ModelAdmin):
    pass


class MultiPageContentAdmin(admin.ModelAdmin):
    pass


admin.site.register(SideBarItems, SideBarAdmin)
admin.site.register(OnePageContent, OnePageContentAdmin)
admin.site.register(MultiPageContent, MultiPageContentAdmin)
