from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.blog.models import Post, Country, Region, Course
from apps.blog.apis.serializers import (
    BlogPostListSerializer,
    CountryPostListSerializer,
    RegionPostListSerializer,
    CoursesPostListSerializer,
)


class BlogPostListAPIView(APIView):
    serializer_class = BlogPostListSerializer

    def get(self, request):
        posts = Post.objects.all()
        serializer = BlogPostListSerializer(posts, many=True)
        return Response({"posts": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogPostListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request):
        pass


class BlogPostDetailAPIView(GenericAPIView):
    serializer_class = BlogPostListSerializer

    def get_object(self):
        return Post.objects.filter(id=self.kwargs["pk"]).first()

    def get(self, request, *args, **kwargs):
        print(self.request.query_params, args, kwargs)
        post = self.get_object()
        return Response({"post": BlogPostListSerializer(post).data})


class CountryPostListAPIView(APIView):
    serializer_class = CountryPostListSerializer

    def get(self, request):
        countries = Country.objects.all()
        serializer = self.serializer_class(countries, many=True)
        return Response({"countries": serializer.data})


class RegionPostListAPIView(APIView):
    serializer_class = RegionPostListSerializer

    def get(self, request):
        regions = Region.objects.select_related("country").all()
        serializer = self.serializer_class(regions, many=True)
        return Response({"regions": serializer.data})


class CoursesPostListAPIView(APIView):
    serializer_class = CoursesPostListSerializer

    def get(self, request):
        courses = Course.objects.all()
        serializer = self.serializer_class(courses, many=True)
        return Response({"courses": serializer.data})