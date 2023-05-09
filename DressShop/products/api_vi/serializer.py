from rest_framework import serializers
from ..models import Product,Category


class ProductListSerializer(serializers.ModelSerializer):
    get_total_price = serializers.CharField(source='total_price',)

    class Meta:
        model = Product
        fields= '__all__'
        extra_fields = ['get_total_price']
        