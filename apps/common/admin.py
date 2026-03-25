from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.common.models import State, Region, Currency, Media


@admin.register(State)
class StateAdmin(ModelAdmin):
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


@admin.register(Region)
class RegionAdmin(ModelAdmin):
    list_display = [
        "id",
        "name",
        "state",
    ]
    search_fields = [
        "name",
    ]
    fields = [
        "name",
        "state",
    ]
    list_filter = [
        "state",
    ]


@admin.register(Currency)
class CurrencyAdmin(ModelAdmin):
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


@admin.register(Media)
class MediaAdmin(ModelAdmin):
    list_display = [
        "id",
        "file",
    ]
    search_fields = [
        "file",
    ]
    fields = [
        "file",
    ]
