from rest_framework.views import APIView, Request, Response, status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from users.permissions import UserIdPermission, UserPermission
from users.serializers import LoginSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from users.models import User


class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get(self, _: Request):
        users = User.objects.all()
        serialized = UserSerializer(users, many=True)

        return Response(serialized.data, status.HTTP_200_OK)


class UserRegisterView(APIView):
    def post(self, request: Request):
        serialized = UserSerializer(data=request.data)

        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)


class UserIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserIdPermission]

    def get(self, _: Request, user_id):
        user = User.objects.get(id=user_id)
        serialized = UserSerializer(user)

        return Response(serialized.data, status.HTTP_200_OK)


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
