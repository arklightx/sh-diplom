from pydoc import Doc
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import DocumentSerializer, DisablingsSerializer
from .models import Disablings, Document


class DocumentView(ReadOnlyModelViewSet):
    queryset = Document.objects.all()
    permission_classes = [AllowAny]
    serializer_class = DocumentSerializer


class DisablingsView(ReadOnlyModelViewSet):
    queryset = Disablings.objects.all()
    permission_classes = [AllowAny]
    serializer_class = DisablingsSerializer

