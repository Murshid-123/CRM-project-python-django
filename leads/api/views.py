from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from leads.models import Lead
from leads.serializers import LeadSerializer
from django.shortcuts import get_object_or_404  


class LeadListAPIView(APIView):
    def get(self, request, format=None):
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LeadDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Lead, pk=pk)

    def get(self, request, pk, format=None):
        lead = self.get_object(pk)
        serializer = LeadSerializer(lead)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        lead = self.get_object(pk)
        serializer = LeadSerializer(lead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        lead = self.get_object(pk)
        lead.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    