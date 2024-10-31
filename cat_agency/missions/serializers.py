from rest_framework import serializers
from .models import Mission, Target

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "name", "country", "notes", "complete"]

    def update(self, instance, validated_data):
        # Check if the target is completed
        if instance.complete:
            raise serializers.ValidationError("Cannot update target because it is completed.")

        # Update fields
        instance.name = validated_data.get("name", instance.name)
        instance.country = validated_data.get("country", instance.country)
        instance.complete = validated_data.get("complete", instance.complete)
        instance.notes = validated_data.get("notes", instance.notes)  # Update notes
        instance.save()

        # Check if the mission is completed
        self.check_mission_completion(instance.mission)

        return instance

    def check_mission_completion(self, mission):
        # Mark the mission as completed if all targets are completed
        if all(target.complete for target in mission.targets.all()):
            mission.complete = True
            mission.save()


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True, required=False)

    class Meta:
        model = Mission
        fields = "__all__"

    def create(self, validated_data):
        targets_data = validated_data.pop("targets", None)

        # Check the number of targets
        if targets_data is not None and (len(targets_data) < 1 or len(targets_data) > 3):
            raise serializers.ValidationError("There must be between 1 and 3 targets.")

        # Create the mission
        mission = Mission.objects.create(**validated_data)

        # Create targets if provided
        if targets_data:
            for target_data in targets_data:
                self.update_or_create_target(mission, target_data)

        return mission

    def update(self, instance, validated_data):
        targets_data = validated_data.pop("targets", None)
        cat = validated_data.get("cat", instance.cat)

        # Check if the cat is assigned to another active mission
        if cat and cat != instance.cat and Mission.objects.filter(cat=cat, complete=False).exists():
            raise serializers.ValidationError("This cat already has an active mission.")

        # Check if the mission is completed
        if instance.complete:
            raise serializers.ValidationError("Cannot update a completed mission.")

        # Update mission fields
        instance.cat = cat
        instance.complete = validated_data.get("complete", instance.complete)
        instance.save()

        # Update or create targets if provided
        if targets_data is not None:
            for target_data in targets_data:
                self.update_or_create_target(instance, target_data)

        # Check mission completion
        self.check_mission_completion(instance)

        return instance

    def update_or_create_target(self, mission, target_data):
        target_name = target_data.get("name")
        
        # Look for the target by name
        target = Target.objects.filter(mission=mission, name=target_name).first()

        if target is not None:
            # If the target exists, update it
            # No completion check here
            target.country = target_data.get("country", target.country)
            target.complete = target_data.get("complete", target.complete)

            # Update notes if provided
            if 'notes' in target_data:
                target.notes = target_data['notes']

            target.save()
        else:
            # Check if the number of targets exceeds 3
            if Target.objects.filter(mission=mission).count() >= 3:
                raise serializers.ValidationError("Cannot have more than 3 targets.")

            # If the target does not exist, create a new one
            target = Target.objects.create(
                mission=mission,
                name=target_name,
                country=target_data.get("country"),
                complete=target_data.get("complete", False),
                notes=target_data.get("notes", ""),
            )

    def check_mission_completion(self, mission):
        # Mark the mission as completed if all targets are completed
        if all(target.complete for target in mission.targets.all()):
            mission.complete = True
            mission.save()