from .models import CustomUser
from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(username=serializer.validated_data['username']).first()
        if not user or not user.check_password(serializer.validated_data['password']):
            return Response({"error": "Invalid credentials"}, status=400)

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "user_id": user.id,
            "username": user.username
        })

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"})

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You unfollowed {user_to_unfollow.username}"})

class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def get_object(self):
        return self.request.user
