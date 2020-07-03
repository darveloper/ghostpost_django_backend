from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'text', 'post_time', 'upvotes', 'downvotes', 'post_choice', 'score']
        