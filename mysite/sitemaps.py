from django.contrib.sitemaps import Sitemap
from django.shortcuts import get_list_or_404, get_object_or_404
from mysite.models import Content, SideBarItems

class MySiteSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = "https"

    def items(self):
        items = get_list_or_404(SideBarItems, display=True)
        return items
