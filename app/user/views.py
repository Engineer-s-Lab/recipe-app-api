from user.serializers import UserSerializer, AuthTokenSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import generics

class CreateUserView(generics.CreateAPIView):
    # Create a new user in the system
    serializer_class = UserSerializer  


class CreateTokenView(ObtainAuthToken):
    # Create a auth token for the user
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES