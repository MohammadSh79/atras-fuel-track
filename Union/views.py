from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Get driver count and send it via serializer
        return Response("Dashboard API View")
    
class MembersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user.certificate_id)
        return Response("Members API View")