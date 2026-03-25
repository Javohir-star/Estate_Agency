from typing import Any

from django.views.generic import TemplateView
from django.shortcuts import redirect

from apps.blog.models import Post, PostComment


class BlogListView(TemplateView):
    template_name = "blog-grid.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        limit, offset = (
            self.request.GET.get("limit", 10),
            self.request.GET.get("offset", 0),
        )
        pages_count = Post.objects.count() // int(limit) + 1
        context["posts"] = Post.objects.select_related("image", "category").order_by(
            "-created_at"
        )[int(offset) : int(offset) + int(limit)]
        context["limit"] = limit
        context["offset"] = offset
        context["posts_count"] = [i + 1 for i in range(pages_count)]
        return context


class BlogSingleView(TemplateView):
    template_name = "blog-single.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        try:
            context["post"] = Post.objects.select_related("image", "category").get(
                slug=slug
            )
        except Post.DoesNotExist:
            context["post"] = None

        comments = PostComment.objects.filter(post=context["post"]).order_by(
            "-created_at"
        )
        context["comments"] = comments
        context["comments_count"] = len(comments)
        return context

    def post(self, request, *args, **kwargs):
        slug = self.kwargs.get("slug")
        name = request.POST.get("inputname", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        errors = {}
        if not name:
            errors["name_error"] = "Name is required."
        if not email or "@" not in email:
            errors["email_error"] = "Enter a valid email address."
        if not message:
            errors["text_error"] = "Message is required."

        if errors:
            context = self.get_context_data(**kwargs)
            context.update(errors)
            return self.render_to_response(context)

        PostComment.objects.create(
            post=Post.objects.get(slug=slug),
            text=message,
            reply_to=None,
        )
        return redirect("blog-single", slug=slug)


class CountryListView(TemplateView):
    template_name = "country.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class RegionListView(TemplateView):
    template_name = "region.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class CourseListView(TemplateView):
    template_name = "courses.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context