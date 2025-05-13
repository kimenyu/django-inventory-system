# accounts/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer, CreateUserSerializer
from .permissions import IsAdminUserCustom

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUserCustom]

    def get_serializer_class(self):
        if self.action in ['create']:
            return CreateUserSerializer
        return UserSerializer
