# API Documentation:
# GET /posts/
# Returns a paginated list of posts, each with:
#   - id, text, timestamp, user (username), comment_count, and up to 3 latest comments (each with text, timestamp, user)
#   - Example response:
#   {
#     "count": 20,
#     "next": "...",
#     "previous": null,
#     "results": [
#       {
#         "id": "...",
#         "text": "...",
#         "timestamp": "...",
#         "user": "...",
#         "comment_count": 5,
#         "comments": [
#           {"id": "...", "text": "...", "timestamp": "...", "user": "..."}, ...
#         ]
#       }, ...
#     ]
#   }
#
# Follow-up Question Answer:
# To fetch 3 random comments for a post instead of latest:
#   Replace obj.comments.order_by('-timestamp')[:3] with obj.comments.order_by('?')[:3] in PostSerializer.get_comments()
#   
#   The '?' in Django's order_by() method tells the database to return results in random order.
#   This is equivalent to SQL's ORDER BY RAND() and will return 3 random comments for each post.
#   
#   Example implementation:
#   def get_comments(self, obj):
#       qs = obj.comments.order_by('?')[:3]  # Random order instead of -timestamp
#       return CommentSerializer(qs, many=True).data

from rest_framework import generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-timestamp')
    serializer_class = PostSerializer

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
