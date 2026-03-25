from django.db.models import TextChoices


class EstateStatusChoices(TextChoices):
    SALE = "sale", "For Sale"
    SOLD = "sold", "Sold"
    RENT = "rent", "For Rent"
    UNAVAILABLE = "unavailable", "Unavailable"
