from rest_framework import serializers
from User.serializers import RealUserSerializer, LegalUserSerializer

class DashboardViewSerializer(serializers.Serializer):
    driver_count = serializers.IntegerField()

class MembersViewSerializer(serializers.Serializer):
    real_users = RealUserSerializer(many=True)
    legal_users = LegalUserSerializer(many=True)