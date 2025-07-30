from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'text', 'timestamp', 'user', 'post']

    def create(self, validated_data):

        from django.contrib.auth.models import User
        user = User.objects.first()
        if not user:

            user = User.objects.create_user(username='demo_user', email='demo@example.com')
        validated_data['user'] = user
        return super().create(validated_data)

class PostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    comment_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'timestamp', 'user', 'comment_count', 'comments']

    def get_comment_count(self, obj):
        return obj.comments.count()

    def get_comments(self, obj):
        qs = obj.comments.order_by('-timestamp')[:3]
        return CommentSerializer(qs, many=True).data

    def create(self, validated_data):

        from django.contrib.auth.models import User
        user = User.objects.first()
        if not user:
            # Create a default user if none exists
            user = User.objects.create_user(username='demo_user', email='demo@example.com')
        validated_data['user'] = user
        return super().create(validated_data)
