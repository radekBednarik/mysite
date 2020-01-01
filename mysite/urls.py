from django.urls import path
from mysite.views import ContentView
from django.views.generic import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(url="about-1/"), name="content"),
    path("<each>-<id>/", ContentView.as_view(), name="content"),
]
