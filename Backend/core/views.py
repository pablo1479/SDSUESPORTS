from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import SDSUESPORTS
from .serializers import ESportsTeamSerializer

class ESportsTeamListCreate(generics.ListCreateAPIView):
    queryset = SDSUESPORTS.objects.all()
    serializer_class = ESportsTeamSerializer
    permission_classes = [IsAuthenticated]

class ESportsTeamRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SDSUESPORTS.objects.all()
    serializer_class = ESportsTeamSerializer
    permission_classes = [IsAuthenticated]
