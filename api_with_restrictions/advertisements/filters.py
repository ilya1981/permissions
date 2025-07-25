from django_filters import rest_framework as filters, DateTimeFromToRangeFilter
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateTimeFromToRangeFilter()
    status_open = filters.OrderingFilter(field_name='open')
    status_close = filters.OrderingFilter(field_name='close')


    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ["creator", "title", "created_at", "status", "favourites"]
