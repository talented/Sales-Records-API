from rest_framework import serializers
from app.models import Sales


class SalesSerializer(serializers.ModelSerializer):

    region = serializers.CharField(max_length=255, required=False)
    country = serializers.CharField(max_length=255, required=False)
    ptype = serializers.CharField(max_length=255, required=False)
    channel = serializers.CharField(max_length=255, required=False)
    date = serializers.DateField(format='%d.%m.%Y', required=False)
    quantity = serializers.IntegerField()
    price = serializers.FloatField()
    cost = serializers.FloatField()
    revenue = serializers.FloatField()
    profit = serializers.FloatField()

    profit_percentage = serializers.DecimalField(
        max_digits=10, decimal_places=2)

    class Meta:
        model = Sales
        fields = ('id', 'region', 'country', 'ptype', 'channel', 'date', 'quantity',
                  'price', 'cost', 'revenue', 'profit', 'profit_percentage')
