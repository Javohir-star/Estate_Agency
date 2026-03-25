from django.db import models
# from ckeditor.fields import RichTextField

from apps.common.models import BaseModel, Media
from core.utils import slugify


class Post(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, verbose_name="Slug", blank=True, null=True)
    subtitle = models.CharField(max_length=255, verbose_name="Subtitle")
    image = models.ForeignKey(
        "common.Media",
        on_delete=models.RESTRICT,
        verbose_name="Image",
        blank=True,
        null=True,
    )
    author = models.CharField(max_length=255, verbose_name="Author")
    category = models.ForeignKey(
        "blog.PostCategory",
        on_delete=models.RESTRICT,
        verbose_name="Category",
    )
    content = models.TextField(verbose_name="Content")
    views_count = models.IntegerField(verbose_name="Views Count", default=0)
    comments_count = models.IntegerField(verbose_name="Comments Count", default=0)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def save(self, *args, **kwargs):
        if self.title and self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Category Name")

    class Meta:
        verbose_name = "Post Category"
        verbose_name_plural = "Post Categories"

    def __str__(self):
        return self.name


class PostComment(BaseModel):
    post = models.ForeignKey(
        "blog.Post",
        on_delete=models.RESTRICT,
        verbose_name="Post",
    )
    text = models.TextField(verbose_name="Text")
    reply_to = models.ForeignKey(
        "blog.PostComment",
        on_delete=models.RESTRICT,
        verbose_name="Reply To",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Post Comment"
        verbose_name_plural = "Post Comments"

    def __str__(self):
        return self.text


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name="Country Name")

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name
    

class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name="Region Name")
    country = models.ForeignKey(
        "blog.Country",
        on_delete=models.RESTRICT,
        verbose_name="Country",
    )

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="Course Name")
    region = models.ForeignKey(
        "blog.Region",
        on_delete=models.RESTRICT,
        verbose_name="Region",
    )

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name