from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Question
from .serializers import QuestionSerializer


class QuestionView(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]
    http_method_names = ["get", "post", "head"]

    def create(self, request: Request, *args, **kwargs):
        try:
            serializer = super().get_serializer(Question.objects.create(**request.data))
            return Response(serializer.data, status=201)
        except Exception as e:
            return Response(status=400)
