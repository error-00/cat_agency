from rest_framework import serializers
from .models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"


class MissionSerializer(serializers.ModelSerializer):
    targets = serializers.PrimaryKeyRelatedField(many=True, queryset=Target.objects.all())

    class Meta:
        model = Mission
        fields = "__all__"
