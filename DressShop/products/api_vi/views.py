from rest_framework.generics import GenericAPIView
from .serializer import *
from rest_framework.views import APIView
from ..models import Product
from rest_framework.response import Response
from rest_framework import status


class ProductListView(APIView):
    serializer_class = ProductListSerializer

    def get(self, request):
        products = Product.objects.all()
        serializer = self.serializer_class(products,many=True)

        return Response(serializer.data)

