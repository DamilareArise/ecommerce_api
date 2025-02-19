from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, get_tokens_for_user
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data= request.data)
        if serializer.is_valid(): 
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                tokens = get_tokens_for_user(user)
                return Response({
                    'id': user.id,
                    'fullname': user.get_full_name,
                    'email': user.email,
                    'access': tokens['access'],
                    'refresh': tokens['refresh']
                })
            return Response({'error':'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
        