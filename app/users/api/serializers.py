from rest_framework import serializers
from users import models as users_models


class UserSerializer(serializers.ModelSerializer):

    nombre = serializers.CharField()
    apellido = serializers.CharField()
    documento = serializers.CharField()
    fecha = serializers.DateField()

    class Meta:
        model = users_models.Usuario
        fields = ("nombre", "apellido", "documento", "fecha")
