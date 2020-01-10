from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class PageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = "https"

    def items(self):
        return ["about_page", "skills_page", "projects_page", "code_page"]

    def location(self, item):
        return reverse(item)

