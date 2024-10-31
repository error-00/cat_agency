from rest_framework import generics
from .models import Mission, Target
from .serializers import MissionSerializer, TargetSerializer


# List of missions
class MissionList(generics.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


# Getting and updating/deleting specifi mission
class MissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

# Creating new mission (POST)
class MissionCreate(generics.CreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


# List of targets
class TargetList(generics.ListCreateAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


# Getting and updating/deleting specifi mission
class TargetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


# Creating new target (POST)
class TargetCreate(generics.CreateAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
