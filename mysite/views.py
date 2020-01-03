from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic.base import TemplateView
from .models import SideBarItems, Content


class ContentView(TemplateView):
    template_name = "mysite/main.html"

    def get_context_data(self, page, **kwargs):
        # for displaying navbar
        items = get_list_or_404(SideBarItems, display=True)
        # for getting the content when clicked on given navbar link
        # the identifier is given by <page> in URLconf
        item = get_object_or_404(SideBarItems, items=str(page).capitalize())

        context = super().get_context_data(**kwargs)
        context["content"] = Content.objects.get(side_bar_item_id=item.id)
        context["sidebar"] = items
        # to be able to switch link styles between active and not active
        context["pageid"] = str(page)
        return context
