from rest_framework import serializers
from .models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = "__all__"

    def create(self, validated_data):
        targets_data = validated_data.pop("targets")
        mission = Mission.objects.create(**validated_data)

        for target_data in targets_data:
            target = Target.objects.create(**target_data)  # Create target
            mission.targets.add(target)

        return mission
