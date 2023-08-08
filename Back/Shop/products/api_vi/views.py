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
from django.conf import settings
import requests
import json


class ProductListView(APIView):
    serializer_class = ProductListSerializer

    def get(self, request):
        products = Product.objects.all()
        serializer = self.serializer_class(products,many=True, context={'request':request})

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

    def get(self, request,id):
        product = Product.objects.get(id=id)
        serializer = ProductDetailSerializer(product)

        return Response(serializer.data)
    
    def post(self, request,id):
        user = request.user
        product = Product.objects.get(id=id)
        comment = Comment(user =user,product = product)
        serializer = CommentSerializer(comment,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('ok')
    



class FavoritListView(APIView):
    def get(self, request):
        favoritlist = Favorit_List.objects.filter(owner = request.user)
        serializer = FavoritListSerializer(favoritlist,many=True)

        return Response(serializer.data)
    

class AddToFavoritListView(APIView):
    serializer_class =AddToFavoritListserializer

    def post(self, request,id):
        product = Product.objects.get(id=id)
        favoritlist = Favorit_List.objects.get(owner = request.user)
        favoritlist.product.add(product)
    

        return Response({"detail":'product is added to favoritlist'})
    
    def delete(self, request,id):
        product = Product.objects.get(id=id)
        favoritlist = Favorit_List.objects.get(owner = request.user)
        favoritlist.product.remove(product)

        return Response({"detail":'product is deleted from favoritlist'})






class CartView(APIView):
    serializer_class = CartCreateSerializer
     

    def get(self, request):
        cart = Cart.objects.filter(owner=request.user)
        serializer= CartSerializer(cart,many=True)

        return Response(serializer.data)
    


    def post(self, request):
        serializer = CartCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        
        # quantity = request.data.get('quantity')
        # print('--------------------',cart)
        # print('**************',quantity)
        
        

        return Response('product is added to cart')
    

    

    
class CartDetailView(APIView):
    serializer_class= UpdateCartSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        try:
            cart = Cart.objects.get(owner=request.user,id=id)
            serializer= CartSerializer(cart)

            return Response(serializer.data)
        except :

            return Response({'error':'you do not have access',
                             'status':status.HTTP_403_FORBIDDEN})
    




    def put(self, request,id):
        carts = Cart.objects.get(owner=request.user ,id=id)
        quantity = request.data.get('quantity')
        carts.quantity =quantity
        carts.save()
        serializer =UpdateCartSerializer(carts,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('succussfully updeted the quantity')
    

    def delete(self, request,id):
        carts = Cart.objects.get(owner=request.user,id=id)
        carts.delete()
        
        return Response('succussfully delete the cart')


    
    

   



class ShoppingCartView(APIView):
    serializer_class =ShoppingCartCreateSerializer

    def get(self, request):
        shopping_cart = ShoppingCart.objects.filter(owner=request.user)
        if shopping_cart.exists():
            serializer = ShoppingCartSerializer(shopping_cart,many=True)
            return Response(serializer.data)
        else:
            return Response({'error':'shoppin car does not exist',
                             'status':status.HTTP_404_NOT_FOUND})
        


    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        shopping_cart = ShoppingCart.objects.filter(owner=request.user)[0]
        
        print(shopping_cart.is_paid)
        # cart = Cart.objects.filter(owner = request.user)
        # totalprice = 0
        # for item in cart:
        #     # print('+++++++++++',item.cart_tatolprice())
        #     totalprice+=item.cart_tatolprice()
        # print('***********++++++++++++',totalprice)   

     
        
        


        return Response('Shopping cart is created')
    

# # django zarinpal webgate 

# if settings.SANDBOX:
#     sandbox = 'sandbox'
# else:
#     sandbox = 'www'

# ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
# ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
# ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"


# amount = 1000  # Rial / Required
# description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# phone = 'YOUR_PHONE_NUMBER'  # Optional
# # Important: need to edit for realy server.
# CallbackURL = 'http://127.0.0.1:8080/verify/'








    
# class SendRequestView(APIView):

#     def post(self, request):
         
#         data = {
#         "MerchantID": settings.MERCHANT,
#         "Amount": amount,
#         "Description": description,
#         "Phone": phone,
#         "CallbackURL": CallbackURL,
#         }
    
#         data = json.dumps(data)
#         headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
#         try:
#             response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)

#             if response.status_code == 200:
#                 response = response.json()
#                 if response['Status'] == 100:
#                     return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']}
#                 else:
#                     return {'status': False, 'code': str(response['Status'])}
#             return response
    
#         except requests.exceptions.Timeout:
#             return {'status': False, 'code': 'timeout'}
#         except requests.exceptions.ConnectionError:
#             return {'status': False, 'code': 'connection error'}

    


# class VerifyView(APIView):
     
#      def get(self, request):
#          return
         