from rest_framework import serializers
from ..models import *


class ProductListSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Product
        # fields= ('id', 'name',)
        fields = '__all__'
        


class ProductDetailSerializer(serializers.ModelSerializer):
    get_total_price = serializers.CharField(source='total_price',)

    class Meta:
        model = Product
        fields= '__all__'
        extra_fields = ['get_total_price']



class CartSerializer(serializers.ModelSerializer):
    # get_cart_price = serializers.CharField(source='cart_price',)
    # get_item_detail = serializers.CharField(source='item_detail',)
    # get_total_items = serializers.CharField(source='total_items',)
    
    # user = serializers.PrimaryKeyRelatedField(read_only=True,default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields= '__all__'
        # extra_fields = ['get_cart_price','get_item_detail','get_total_items ']




class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model  = CartItems
        fields = '__all__'

class CartItemDetailSerializer(serializers.ModelSerializer):
    item_price = serializers.CharField(source='item.price')
    item_name = serializers.CharField(source='item.name')
    item_size = serializers.CharField(source='item.size')
    item_color = serializers.CharField(source='item.color')

    class Meta:
        model= Cart
        fields = ('item_name','item_price','quantity','item_size','item_color')


class AddCartSerializer(serializers.ModelSerializer):

    class Meta:
        model= Cart
        fields = '__all__'


