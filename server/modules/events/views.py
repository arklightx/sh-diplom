from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from modules.events.models import Events
from modules.events.serializers import EventSerializer


class EventViews(viewsets.ReadOnlyModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        raise Exception("asd")

    def retrieve(self, request, *args, **kwargs):
        return Response(self.serializer_class(Events.objects.filter(home_id=kwargs["pk"]), many=True).data)
