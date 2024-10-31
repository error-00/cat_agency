from rest_framework import serializers
from .models import SpyCat
from .fetch_breeds import fetch_cat_breeds


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = "__all__"
    
    def validate_breed(self, value):
        # Getting list of breed from TheCatAPI
        breeds = fetch_cat_breeds()
        if breeds is None:
            raise serializers.ValidationError("Error in obtaining breeds.")
        
        # Check if the specific breed is on the list
        if value.lower() not in breeds:
            raise serializers.ValidationError(f"Breed '{value}' not found")
        
        return value
    

    def update(self, instance, validated_data):
        # Check if updating only salary
        if 'salary' in validated_data:
            instance.salary = validated_data['salary']
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("Only the 'salary' can be updated.")
        
