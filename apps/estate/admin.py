from django.contrib import admin

from apps.estate.models import (
    Amenities,
    Estate,
    EstateAgent,
    EstateAgentComment,
    EstateCategory,
)


@admin.register(EstateAgent)
class EstateAgentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "phone",
        "email",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "email",
        "phone",
    ]
    fields = [
        "first_name",
        "last_name",
        "bio",
        "avatar",
        "phone",
        "mobile",
        "email",
        "telegram",
        "whatsapp",
        "instagram",
        "facebook",
        "x",
    ]


@admin.register(EstateCategory)
class EstateCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    search_fields = [
        "name",
    ]
    fields = [
        "name",
    ]


@admin.register(Amenities)
class AmenitiesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    search_fields = [
        "name",
    ]
    fields = [
        "name",
    ]


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "agent",
        "category",
        "state",
        "region",
        "status",
        "price",
        "currency",
    ]
    list_filter = [
        "status",
        "category",
        "state",
        "region",
        "currency",
    ]
    search_fields = [
        "name",
        "address",
    ]
    filter_horizontal = [
        "amenities",
        "images",
    ]
    fields = [
        "name",
        "agent",
        "category",
        "state",
        "region",
        "address",
        "latitude",
        "longitude",
        "status",
        "area",
        "beds",
        "baths",
        "garage",
        "price",
        "currency",
        "description",
        "amenities",
        "images",
        "video",
    ]


@admin.register(EstateAgentComment)
class EstateAgentCommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
    ]
    search_fields = [
        "name",
        "email",
    ]
    fields = [
        "name",
        "email",
        "comment",
    ]
