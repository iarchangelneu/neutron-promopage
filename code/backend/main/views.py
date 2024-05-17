from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .models import Application
from .serializers import ApplicationSerializer

class NewApplication(CreateAPIView):
    permission_classes = [AllowAny,]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    