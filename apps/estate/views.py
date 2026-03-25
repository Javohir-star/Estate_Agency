from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, RedirectView

from apps.estate.models import Estate


def home(request):
    estates = Estate.objects.prefetch_related("images").all()
    return render(request, "estate/index.html", context={"estates": estates})


def about(request):
    return render(request, "about.html")


class PropertyView(TemplateView):
    template_name = "property-grid.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["estates"] = Estate.objects.prefetch_related("images").all()
        return context


class BlogListView(TemplateView):
    template_name = "blog-grid.html"


class PropertySingleView(TemplateView):
    template_name = "property-single.html"


class BlogSingleView(TemplateView):
    template_name = "blog-single.html"


class AgentListView(TemplateView):
    template_name = "agents-grid.html"


class AgentSingleView(TemplateView):
    template_name = "agent-single.html"


class ContactView(TemplateView):
    template_name = "contact.html"
