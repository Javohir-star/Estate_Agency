from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.common.models import BaseModel
from apps.estate.choices import EstateStatusChoices


class EstateAgent(BaseModel):
    first_name = models.CharField(max_length=255, verbose_name="First Name")
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    bio = models.TextField(verbose_name="Bio", blank=True, null=True)
    avatar = models.ForeignKey(
        "common.Media",
        verbose_name="Avatar",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
    )
    phone = models.CharField(max_length=255, verbose_name="Phone")
    mobile = models.CharField(
        max_length=255, verbose_name="Mobile", blank=True, null=True
    )
    email = models.EmailField(verbose_name="Email")
    telegram = models.CharField(
        max_length=255, verbose_name="Telegram", blank=True, null=True
    )
    whatsapp = models.CharField(
        max_length=255, verbose_name="WhatsApp", blank=True, null=True
    )
    instagram = models.CharField(
        max_length=255, verbose_name="Instagram", blank=True, null=True
    )
    facebook = models.CharField(
        max_length=255, verbose_name="Facebook", blank=True, null=True
    )
    x = models.CharField(max_length=255, verbose_name="X", blank=True, null=True)

    class Meta:
        verbose_name = "Estate Agent"
        verbose_name_plural = "Estate Agents"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Estate(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Estate Name")
    agent = models.ForeignKey(
        "estate.EstateAgent",
        on_delete=models.RESTRICT,
        related_name="estates",
        verbose_name="Estate Agent",
    )
    category = models.ForeignKey(
        "estate.EstateCategory",
        on_delete=models.RESTRICT,
        related_name="estates",
    )
    state = models.ForeignKey(
        "common.State",
        on_delete=models.RESTRICT,
        related_name="estates",
    )
    region = models.ForeignKey(
        "common.Region",
        on_delete=models.RESTRICT,
        related_name="estates",
    )
    address = models.CharField(max_length=255, verbose_name="Address")
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name="Latitude"
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name="Longitude"
    )
    status = models.CharField(
        max_length=255, verbose_name="Status", choices=EstateStatusChoices.choices
    )
    area = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="Area (m^2)"
    )
    beds = models.IntegerField(
        verbose_name="Beds", validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    baths = models.IntegerField(
        verbose_name="Baths", validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    garage = models.IntegerField(
        verbose_name="Garage", validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    currency = models.ForeignKey(
        "common.Currency",
        on_delete=models.RESTRICT,
        related_name="estates",
    )
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    amenities = models.ManyToManyField(
        "estate.Amenities", verbose_name="Amenities", related_name="estates"
    )
    images = models.ManyToManyField(
        "common.Media", verbose_name="Images", related_name="estates"
    )
    video = models.URLField(verbose_name="Video", blank=True, null=True)

    class Meta:
        verbose_name = "Estate"
        verbose_name_plural = "Estates"

    def __str__(self):
        return self.name


class EstateCategory(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Estate Category Name")

    class Meta:
        verbose_name = "Estate Category"
        verbose_name_plural = "Estate Categories"

    def __str__(self):
        return self.name


class Amenities(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Amenity Name")

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"

    def __str__(self):
        return self.name


class EstateAgentComment(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    comment = models.TextField(verbose_name="Comment")

    class Meta:
        verbose_name = "Estate Agent Comment"
        verbose_name_plural = "Estate Agent Comments"

    def __str__(self):
        return self.name
