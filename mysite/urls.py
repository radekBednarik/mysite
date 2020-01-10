from django.urls import path, re_path
from mysite.views import AboutView, SkillsView, ProjectsView, CodeView
from django.views.generic import RedirectView
from mysite.sitemaps import PageSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {"PageMap": PageSitemap}

urlpatterns = [
    path("", RedirectView.as_view(url="about/"), name="content"),
    path(
        "about/",
        AboutView.as_view(template_name="mysite/onepage.html"),
        name="about_page",
    ),
    path(
        "skills/",
        SkillsView.as_view(template_name="mysite/onepage.html"),
        name="skills_page",
    ),
    path(
        "projects/",
        ProjectsView.as_view(template_name="mysite/multipage.html"),
        name="projects_page",
    ),
    path(
        "code/",
        CodeView.as_view(template_name="mysite/multipage.html"),
        name="code_page",
    ),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
