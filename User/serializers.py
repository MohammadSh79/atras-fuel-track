from rest_framework.serializers import ModelSerializer
from .models import User, RealUser, LegalUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LegalUserSerializer(ModelSerializer):
    class Meta:
        model = LegalUser
        fields = '__all__'

class RealUserSerializer(ModelSerializer):
    class Meta:
        model = RealUser
        fields = '__all__'