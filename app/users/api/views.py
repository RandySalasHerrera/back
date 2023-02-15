from rest_framework import generics, status
from rest_framework.response import Response
from users import models as users_models
from users.api import serializers
from users import exceptions

#from keycloak import KeycloakOpenID

class UserAPIView(generics.ListAPIView):

    # keycloak_roles = {
    #     'GET': ['Admin'],
    # }

    # Configure client


    serializer_class = serializers.UserSerializer
    
    # def get_queryset(self):
    #     return users_models.User.objects.all()

    def get(self, request, format=None):

        return Response(data={'status': '201', 'message': 'lista de usuario'})


    def post(self, request, format=None):

        id = self.request.data.get("id", None)
        name = self.request.data.get("name", None)

        validadet_user = users_models.User.objects.filter(name=name).last()

        if validadet_user:
            raise exceptions.UserAlreadyRegister()

        user = users_models.User.objects.create(id=id,
                                                name=name,
                                                )
        user.save()

        return Response(data={'status': '201', 'message': 'usuario creado correctamente'})

