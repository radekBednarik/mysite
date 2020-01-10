from datetime import datetime as dt

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import MultiPageContent, OnePageContent, SideBarItems


class AboutView(TemplateView):
    template_name = "mysite/onepage.html"

    def get_context_data(self, **kwargs):
        id_ = SideBarItems.objects.get(items="About")
        context = super().get_context_data(**kwargs)
        context["now"] = dt.now()
        context["content"] = OnePageContent.objects.get(side_bar_item_id=id_)
        return context


class SkillsView(TemplateView):
    template_name = "mysite/onepage.html"

    def get_context_data(self, **kwargs):
        id_ = SideBarItems.objects.get(items="Skills")
        context = super().get_context_data(**kwargs)
        context["now"] = dt.now()
        context["content"] = OnePageContent.objects.get(side_bar_item_id=id_)
        return context


class ProjectsView(ListView):
    template_name = "mysite/multipage.html"
    paginate_by = 2
    model = MultiPageContent

    def get_queryset(self):
        id_ = SideBarItems.objects.get(items="Projects")
        return MultiPageContent.objects.filter(side_bar_item_id=id_).order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = dt.now()
        return context


class CodeView(ListView):
    template_name = "mysite/multipage.html"
    paginate_by = 2
    model = MultiPageContent

    def get_queryset(self):
        id_ = SideBarItems.objects.get(items="Code")
        return MultiPageContent.objects.filter(side_bar_item_id=id_).order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = dt.now()
        return context
