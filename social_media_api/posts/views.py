from rest_framework import viewsets, permissions, authentication, filters, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.contenttypes.models import ContentType
from notifications.utils import create_notification
from notifications.models import Notification

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit/delete it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method in permissions.SAFE_METHODS

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# view to generate feeds based on user followed
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def user_feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# view to like post
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    # post = Post.objects.filter(pk=pk).first() # ALX wahala
    post = generics.get_object_or_404(Post, pk=pk)
    if not post:
        return Response({"error": "Post not found."}, status=404)

    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        return Response({"detail": "Already liked."}, status=400)

    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author, 
            actor=request.user, 
            verb='liked', 
            target=post,
            content_type=ContentType.objects.get_for_model(post),
            object_id=post.id
        )
        # create_notification(recipient=post.author, actor=request.user, verb='liked', target=post)

    return Response({"detail": "Post liked."})

# view to unlike a post
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    like = Like.objects.filter(user=request.user, post_id=pk).first()
    if not like:
        return Response({"detail": "You haven't liked this post."}, status=400)
    
    like.delete()
    return Response({"detail": "Post unliked."})

