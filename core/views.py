from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics



# Create your views here.
class UserView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    parser_classes=[IsAuthenticated]

