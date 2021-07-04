from django.urls import path
from . import views
from .views import FormationViewSet, CourseViewSet, ExerciseViewSet

urlpatterns = [
    path("formation" , FormationViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('formation/<str:pk>', FormationViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("course" , CourseViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('course/<str:pk>', CourseViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("exercise" , ExerciseViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('exercise/<str:pk>', ExerciseViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
]
