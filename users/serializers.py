from django.db.models.fields import DateTimeCheckMixin
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import User
import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'gender',
            'email',
            'avatar',
            'password',
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }
