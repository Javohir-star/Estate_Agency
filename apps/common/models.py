from django.db import models
from django.utils import timezone


def media_upload_to(_instance, filename):
    return timezone.now().strftime(f"media/%Y/%m/%d/{filename}")


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Media(BaseModel):
    file = models.FileField(
        verbose_name="Media",
        upload_to=media_upload_to,
    )

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"

    def __str__(self):
        return self.file.name


class State(models.Model):
    name = models.CharField(max_length=255, verbose_name="State Name")

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return self.name


class Region(models.Model):
    state = models.ForeignKey(
        "common.State",
        on_delete=models.RESTRICT,
        related_name="regions",
    )
    name = models.CharField(max_length=255, verbose_name="Region Name")

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=255, verbose_name="Currency Name")

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Service Name")
    icon = models.ForeignKey(
        "common.Media",
        on_delete=models.RESTRICT,
        verbose_name="Icon",
    )

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name
