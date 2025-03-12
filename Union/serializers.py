from rest_framework import serializers

class DashboardSerializer(serializers.Serializer):
    driver_count = serializers.IntegerField()