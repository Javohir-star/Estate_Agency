from django.urls import path

from apps.blog.views import (
    BlogListView,
    BlogSingleView,
    CountryListView,
    RegionListView,
    CourseListView,
)
from apps.blog.apis.views import (
    BlogPostListAPIView,
    BlogPostDetailAPIView,
    CountryPostListAPIView,
    RegionPostListAPIView,
    CoursesPostListAPIView,
)


urlpatterns = [
    path("posts/", BlogListView.as_view(), name="blogs"),
    path("posts/<slug:slug>/", BlogSingleView.as_view(), name="blog-single"),
    path("api/posts/", BlogPostListAPIView.as_view(), name="api-blogs"),
    path("api/post/<int:pk>/", BlogPostDetailAPIView.as_view(), name="api-blog-single"),
    path("countries/", CountryListView.as_view(), name="countries"),
    path("regions/", RegionListView.as_view(), name="regions"),
    path("courses/", CourseListView.as_view(), name="courses"),
    path("api/countries/", CountryPostListAPIView.as_view(), name="api-countries"),
    path("api/regions/", RegionPostListAPIView.as_view(), name="api-regions"),
    path("api/courses/", CoursesPostListAPIView.as_view(), name="api-courses"),
]
