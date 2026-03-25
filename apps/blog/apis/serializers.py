from rest_framework import serializers

from apps.blog.models import Post, Country, Region, Course


class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "slug", "created_at"]


class CountryPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["name"]


class RegionPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["name", "country"]


class CoursesPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["name", "region"]
