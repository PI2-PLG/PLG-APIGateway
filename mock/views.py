from rest_framework import generics
from .models import Mock
from .serializers import MockSerializer

# Create your views here.
class MockData(generics.ListCreateAPIView):

    queryset = Mock.objects.all()
    serializer_class = MockSerializer