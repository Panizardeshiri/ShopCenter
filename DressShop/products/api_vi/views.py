from rest_framework.generics import GenericAPIView
from .serializer import *
from rest_framework.views import APIView
from ..models import Product
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User

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

        

