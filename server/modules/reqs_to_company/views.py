from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Requests
from .serializers import RequestsSerializer


class RequestsView(ModelViewSet):
    queryset = Requests.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = RequestsSerializer

    def retrieve(self, request, *args, **kwargs):
        home_id = kwargs.get("pk")
        reqs = Requests.objects.filter(home_id=home_id)
        data = self.serializer_class(reqs, many=True).data
        return Response(data)
