from rest_framework import generics, status
from rest_framework.response import Response
from users import models as users_models
from users.api import serializers

class UserAPIView(generics.ListAPIView):

    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return users_models.Usuario.objects.all()

    def post(self, request, format=None):
        try:
            nombre = self.request.data.get('nombre')
            apellido = self.request.data.get('apellido')
            documento = self.request.data.get('documento')
            fecha = self.request.data.get('fecha')
            usuario = users_models.Usuario.objects.create(
                nombre=nombre,
                apellido=apellido,
                documento=documento,
                fecha=fecha
            )
            usuario.save()
            return Response(data={'status': '201', 'message': 'Usuario creado correctamente'})
        except Exception as e:
            return Response(data={'status': '500', 'message': str(e)}, status=500)
        

