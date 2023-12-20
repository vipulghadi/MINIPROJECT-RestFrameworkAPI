from rest_framework import serializers
from .models import StudentProfile
class StudentProfileSeri(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    email=serializers.CharField(max_length=100)
    nickname=serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return StudentProfile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nickname=validated_data.get("nickname",instance.nickname)
        instance.name=validated_data.get("name",instance.name)
        instance.save()
        return instance
    
    # def validate_name(self,name):
    #     if str(name).startswith("x"):
    #         raise serializers.ValidationError("invalid name")
    #     return name
    
    def validate(self, attrs):
        name=attrs["name"]
        if len(name)<3: raise serializers.ValidationError("name length should be graeter than 2")
        return attrs
        
        
    