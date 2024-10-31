from rest_framework import generics, status
from rest_framework.response import Response
from .models import Mission, Target
from .serializers import MissionSerializer


# List of missions
class MissionList(generics.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


# Getting and updating/deleting specifi mission
class MissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def delete(self, request, *args, **kwargs):
        mission = self.get_object()

        # Checking if it relates with cat
        if mission.cat:
            return Response(
                {"detail": "The mission cannot be deleted because it involves a cat."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # If not, delete
        mission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


