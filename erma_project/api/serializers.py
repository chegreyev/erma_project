from rest_framework import serializers
from .models import Project
from django.contrib.auth import get_user_model

class ProjectSerializer(serializers.ModelSerializer):
    Person = get_user_model()


    project_manager = serializers.SlugRelatedField(
        many = False ,
        slug_field= "id",
        queryset = Person.objects.all()
    )

    developer = serializers.SlugRelatedField(
        many = False , 
        slug_field= "id",
        queryset = Person.objects.all(), 
        allow_null = True
    )

    class Meta:
        model = Project
        fields = ['id' , 'title' , 'cost' , 'description' , 'deadline' , 'developer' , 'project_manager' , 'progress' ]


    def create(self , validated_data):
        project = self.Meta.model(**validated_data)
        project.save()
        return project