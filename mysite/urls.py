from django.urls import path
from mysite.views import ContentView
from django.views.generic import RedirectView
from mysite.sitemaps import MySiteSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {"mysite": MySiteSitemap}

urlpatterns = [
    path("", RedirectView.as_view(url="about/"), name="content_main"),
    path("<page>/", ContentView.as_view(), name="content"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap")
]
