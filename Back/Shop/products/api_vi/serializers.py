from rest_framework import serializers
from ..models import *


class ProductListSerializer(serializers.ModelSerializer):
    is_like = serializers.SerializerMethodField(method_name='get_is_like')
    class Meta:
        model = Product
        fields = '__all__'
        extra_fields = ['is_like']
    def get_is_like(self, instance):
        try:
            user = self.context['request'].user
            favorit_product = Favorit_List.objects.get(owner= user).product.all().values_list('id', flat=True)
            print('*********', favorit_product)

            if instance.id in favorit_product:
                return True
            return False
        except:
            return False
        

    
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['body','created_at'] 

        



class ProductDetailSerializer(serializers.ModelSerializer):
    get_total_price = serializers.CharField(source='total_price',)
    comments = CommentSerializer(read_only=True,many =True)

    
    class Meta:
        model = Product
        fields= '__all__'
        extra_fields = ['get_total_price','comments']


class FavoritListSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.phone')
    product = ProductDetailSerializer(many=True)
    
    
    class Meta:
         model = Favorit_List
         fields = '__all__'
         extra_fields =['owner_name','product']


class AddToFavoritListserializer(serializers.ModelSerializer):
    class Meta:
         model = Favorit_List
         fields = '__all__'



class CartSerializer(serializers.ModelSerializer):
   get_totalprice = serializers.CharField(source='cart_tatolprice',)
   item_name = serializers.CharField(source='item',read_only=True)
   owner_name = serializers.CharField(source='owner.phone')


   class Meta:

        model = Cart
        fields= ('id','owner_name','quantity','item_name','get_totalprice')
        

class CartCreateSerializer(serializers.ModelSerializer):
    # item_name = serializers.CharField(source='item')

    class Meta:
        model =Cart
        fields ='__all__'

class ShoppingCartSerializer(serializers.ModelSerializer):
    cart = CartSerializer(many=True)
    class Meta:
        model = ShoppingCart
        fields = '__all__'
        extra_fields = ['cart']


class ShoppingCartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ('owner','cart')



class UpdateCartSerializer(serializers.ModelSerializer):
    # ids = serializers.IntegerField(read_only=True)
  
    class Meta:
        model = Cart
        fields =('owner','item','quantity')
        

# class DeleteCartSerializer(serializers.ModelSerializer):

#     class Meta:

#         model = Cart
#         fields= ('id',)














# class CartItemDetailSerializer(serializers.ModelSerializer):
#     item_price = serializers.CharField(source='item.price')
#     item_name = serializers.CharField(source='item.name')
#     item_size = serializers.CharField(source='item.size')
#     item_color = serializers.CharField(source='item.color')

#     class Meta:
#         model= Cart
#         fields = ('item_name','item_price','quantity','item_size','item_color')


# class AddCartSerializer(serializers.ModelSerializer):

#     class Meta:
#         model= Cart
#         fields = '__all__'


