from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework.views import APIView
from ..models import *
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication 


class ProductListView(APIView):
    serializer_class = ProductListSerializer

    def get(self, request):
        products = Product.objects.all()
        serializer = self.serializer_class(products,many=True)

        return Response(serializer.data)
    
    

   
    def post(self, request):
        if request.user.is_superuser:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            print(serializer.data)
            return Response({
                'status':status.HTTP_201_CREATED,
                'message':'Product is created'
            }
                )
        
        else:
            return Response({
                'status': status.HTTP_403_FORBIDDEN,
                'message':'You are not allowed'

            })
    
    

            
     






class ProductDetailView(APIView):
    serializer_class = ProductDetailSerializer

    def get(self, request,id):
        product = Product.objects.get(id=id)
        serializer = self.serializer_class(product)

        return Response(serializer.data)

from rest_framework import authentication

class CartView(APIView):
    serializer_class = CartSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    # authentication_classes = (SessionAuthentication,BasicAuthentication)

    def get(self, request):
        # user = User.objects.get(id =id)
        # user = User.objects.get(phone = request.user.phone)
        # print(user.phone)
        user = self.request.user
        print('----------------------',request.headers, user)
        cart = Cart.objects.filter(owner=request.user.id)
        serializer = self.serializer_class(cart,many=True)

        return Response(serializer.data)  


    # def post(self,request):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response('ok')     

class CartItemDetailView(APIView):
    serializer_class =  CartItemDetailSerializer

    def get(self, request,id):
        item = Cart.objects.get(id=id)
        serializer = self.serializer_class(item)

        return Response(serializer.data)
  
class AddCartView(APIView):
    serializer_class = AddCartSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('ok')
    


class CartItemView(APIView):
    serializer_class = CartItemSerializer

    def get(self, request):
        items = CartItems.objects.filter(owner=request.user)
        serializer = self.serializer_class(items,many=True)
        print(serializer.data)

        return Response(serializer.data)
    

    def post(self, request):
        data = request.data
        user = request.user
        cart = Cart.objects.get(owner = user)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        total_price = 0 
        cart_items = CartItems.objects.filter(owner=user ,cart =cart.id)
        # print(len(cart_items))
        for items in cart_items:
            total_price += items.price

        # total_quantity=0
        # for items in cart_items:
        #     total_quantity +=items.quantity     

        cart.cart_totalprice=total_price
        cart.cart_totalquantity = len(cart_items)
        cart.save()
        return Response('ok')


