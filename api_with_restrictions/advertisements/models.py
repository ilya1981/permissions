from alembic.util import status
from django.conf import settings
from django.db import models



class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""

    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"

class AdvertisementFavourites(models.TextChoices):
    FAVOURITES = "FAVOURITES", "Избранное"
    NO_FAVOURITES = "NO FAVOURITES", "Не избранное"



class Advertisement(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN,
    )
    favourites = models.TextField(
        choices=AdvertisementFavourites.choices,
        default=AdvertisementFavourites.NO_FAVOURITES
    )



    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
