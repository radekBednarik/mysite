from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic.base import TemplateView
from .models import SideBarItems, Content


class ContentView(TemplateView):
    template_name = "mysite/main.html"

    def get_context_data(self, id, **kwargs):
        item = get_object_or_404(SideBarItems, pk=id, display=True)
        items = get_list_or_404(SideBarItems, display=True)
        context = super().get_context_data(**kwargs)
        context["content"] = Content.objects.get(side_bar_item_id=item.id)
        context["sidebar"] = items
        context["id"] = int(id)
        return context
