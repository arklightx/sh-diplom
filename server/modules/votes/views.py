from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Votes, VotesVariants
from .serializers import VotesSerializer, VotesVariantsSerializer, CreateVoteSerializer
import json


class CreateVoteView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CreateVoteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
        return Response(serializer.data)


class VotesViews(ReadOnlyModelViewSet):
    queryset = Votes.objects.filter(isActive=True)
    serializer_class = VotesSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        raise Exception('asdasd')

    def retrieve(self, request, *args, **kwargs):
        home_id = kwargs["pk"]
        user_id = request.user.id
        data = self.serializer_class(Votes.objects.filter(isActive=True, home_id=home_id), many=True).data
        jsona = json.loads(json.dumps(data))
        for item in jsona:
            for i, variant in enumerate(item["variants"]):
                is_vote_by_me = user_id in variant["user"]
                if is_vote_by_me:
                    item["userVariant"] = variant["label"]
                cnt_user = len(variant["user"])
                item["variants"][i]["votes"] = cnt_user
            if "userVariant" not in item:
                item["userVariant"] = None
        return Response(jsona)


class VotesVariantsViews(ModelViewSet):
    queryset = VotesVariants.objects.all()
    serializer_class = VotesVariantsSerializer
    permission_classes = [IsAuthenticated]
