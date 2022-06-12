from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)

        data.update({'user': {'username': self.user.username,
                              'email': self.user.email,
                              'first_name': self.user.first_name,
                              'last_name': self.user.last_name,
                            #   'type_user': self.user.get_type_user_display(),
                              } 
                    })

        return data
