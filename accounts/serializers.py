from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        
    
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name = validated_data['first_name'],
            last_name =  validated_data['last_name'],
            email =  validated_data['email'],
            password = validated_data['password']
        )

        return user
    
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, min_length=None, required=True)
    password = serializers.CharField(max_length=128, min_length=8, required=True)
    
    
    
def get_tokens_for_user(user):
    """
    Generate JWT tokens for a user.
    """
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
