from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from users import models as base_models


class UserSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    name = serializers.CharField()

    class Meta:
        model = base_models.User
        fields = ("id", "name")
