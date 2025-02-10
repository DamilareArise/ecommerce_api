from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# APIView
# GenericVIew
# viewSet

class ProductView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            product = get_object_or_404(Product, pk=pk)
            many = False
            
        else:
            
            product = Product.objects.all()
            many = True
            
            
        serializer = ProductSerializer(product, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk=None):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({"message": "Product added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            return Response({"message":'Product updated successfully', "data":serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        
        return Response({"message":"Product deleted successfully"}, status=status.HTTP_200_OK)
        