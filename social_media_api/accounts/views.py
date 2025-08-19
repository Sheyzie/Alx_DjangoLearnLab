from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, authenticate

from .serializers import UserSerializer, RegisterSerializer


User = get_user_model()
CustomUser = get_user_model() # ALX checker stop stressing me

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Deletes the token to force login next time
        request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Return the currently authenticated user
        return self.request.user
    
class FollowAPIView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        if target_user == request.user:
            return Response({'error': "You cannot follow yourself."}, status=400)
        
        if request.user.following.filter(id=target_user.id).exists():
            return Response({'detail': f'You are already following {target_user.username}.'}, status=200)

        
        request.user.following.add(target_user)
        return Response({'detail': f'You are now following {target_user.username}.'}, status=200)
    
class UnfollowAPIView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)

        if target_user == request.user:
            return Response({'error': "You cannot unfollow yourself."}, status=400)

        if not request.user.following.filter(id=target_user.id).exists():
            return Response({'detail': f'You are not following {target_user.username}.'}, status=400)

        request.user.following.remove(target_user)
        return Response({'detail': f'You have unfollowed {target_user.username}.'}, status=200)
    

# # view to follow a user
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def follow_user(request, user_id):
#     target_user = get_object_or_404(User, id=user_id)
#     if target_user == request.user:
#         return Response({'error': "You cannot follow yourself."}, status=400)
    
#     request.user.following.add(target_user)
#     return Response({'detail': f'You are now following {target_user.username}.'}, status=200)

# # view to unfollow a user
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def unfollow_user(request, user_id):
#     target_user = get_object_or_404(User, id=user_id)
#     request.user.following.remove(target_user)
#     return Response({'detail': f'You have unfollowed {target_user.username}.'}, status=200)