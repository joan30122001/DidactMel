from django.db import models
from .models import Formation, Course, Exercise
from rest_framework import serializers

class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields = '__all__'
        

class CourseSerializer(serializers.ModelSerializer):
    formation = FormationSerializer(many = False)
    
    class Meta:
        model = Course
        fields = '__all__'
        
    
class ExerciseSerializer(serializers.ModelSerializer):
    formation = FormationSerializer(many = False)
    course = CourseSerializer(many = False)
    
    class Meta:
        model = Exercise
        fields = '__all__'