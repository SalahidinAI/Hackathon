from .models import *
from .serializers import *
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            refresh_token = serializer.validated_data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({'detail': 'Невалидный токен'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # pagination_class = GenrePagination
    # page_size_query_param = 'page_size'
    # max_page_size = 1000


# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
#
#
# class APIView(generics.ListAPIView):
#     queryset = .objects.all()
#     serializer_class = Serializer
