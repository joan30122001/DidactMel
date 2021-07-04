from django.shortcuts import render
from .models import Formation, Course, Exercise
from .serializers import FormationSerializer, CourseSerializer, ExerciseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from datetime import date, timedelta, datetime
from django.db.models import F
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.

class FormationViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = FormationSerializer(Formation.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        formation = Formation.objects.get(id=pk)
        serializer = FormationSerializer(formation)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = ForamtionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        formation = Formation.objects.get(id=pk)
        serializer = FormationSerializer(instance=formation, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        formation = Formation.objects.get(id=pk)
        formation.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class CourseViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = CourseSerializer(Course.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        course = Course.objects.get(id=pk)
        serializer = CourseSerializer(course)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = ForamtionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        course = Course.objects.get(id=pk)
        serializer = CourseSerializer(instance=course, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        course = Course.objects.get(id=pk)
        course.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
class ExerciseViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = ExerciseSerializer(Exercise.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        exercise = Exercise.objects.get(id=pk)
        serializer = ExerciseSerializer(exercice)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = ForamtionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        exercise = Exercise.objects.get(id=pk)
        serializer = ExerciseSerializer(instance=exercise, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        exercise = Exercise.objects.get(id=pk)
        exercise.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)