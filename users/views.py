from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import RegisterSerializer


class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        password = data.pop("password")
        user = serializer.save(is_active=True)
        user.set_password(password)
        user.save()
