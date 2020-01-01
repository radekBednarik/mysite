from django.contrib import admin
from .models import SideBarItems, Content


class SideBarAdmin(admin.ModelAdmin):
    pass


class ContentAdmin(admin.ModelAdmin):
    pass


admin.site.register(SideBarItems, SideBarAdmin)
admin.site.register(Content, ContentAdmin)
