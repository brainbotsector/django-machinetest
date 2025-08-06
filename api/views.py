from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project
from .serializers import (
    ClientSerializer,
    ClientDetailSerializer,
    ClientCreateSerializer,
    ProjectSerializer,
    ProjectCreateSerializer,
    UserSerializer
)
from django.contrib.auth.models import User

class ClientListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Client.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClientSerializer
        return ClientCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClientDetailSerializer
        return ClientCreateSerializer

class ProjectCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectCreateSerializer
    
    def perform_create(self, serializer):
        client_id = self.kwargs['id']
        client = Client.objects.get(id=client_id)
        serializer.save(client=client, created_by=self.request.user)

class UserProjectListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        return self.request.user.projects.all()