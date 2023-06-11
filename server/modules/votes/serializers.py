from rest_framework import serializers
from .models import Votes, VotesVariants


class CreateVoteSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    home = serializers.IntegerField()
    variants = serializers.ListSerializer(child=serializers.CharField())
    theme = serializers.CharField(max_length=400)

    def create(self, validated_data):
        vote = Votes.objects.create(
            user_id=validated_data["user"],
            home_id=validated_data["home"],
            theme=validated_data["theme"]
        )
        variants = []
        for i in validated_data["variants"]:
            var = VotesVariants.objects.create(label=i, for_vote_id=vote.id)
            variants.append(var)
        vote.variants.set(variants)
        return validated_data


class VotesVariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotesVariants
        fields = "__all__"


class VotesSerializer(serializers.ModelSerializer):
    variants = VotesVariantsSerializer(many=True, read_only=True)

    class Meta:
        model = Votes
        fields = "__all__"
