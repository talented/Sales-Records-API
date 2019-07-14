from rest_framework.generics import ListAPIView
from app.models import Sales
from .serializers import SalesSerializer
from .filters import SalesFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class SalesListAPIView(ListAPIView):
    serializer_class = SalesSerializer
    queryset = Sales.objects.calculated_quantity()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = SalesFilter

    fields = ('id', 'region', 'country', 'ptype', 'channel', 'date', 'quantity',
              'price', 'cost', 'revenue', 'profit', 'profit_percentage')
    filter_fields = fields
    search_fields = fields
