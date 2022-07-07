from rest_framework.views import APIView, Request, Response, status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from users.permissions import UserIdPermission, UserPermission
from users.serializers import LoginSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication


class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def post(self, request: Request):
        serialized = UserSerializer(data=request.data)

        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)

    def get():
        ...


class UserIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserIdPermission]

    def get():
        ...


class UserLogin(APIView):
    def post(self, request: Request):
        serialized = LoginSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        user = authenticate(**serialized.data)

        if not user:
            return Response(
                {"detail": "invalid email or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"Token": token.key}, status=status.HTTP_200_OK)
