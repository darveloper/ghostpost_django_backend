from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class PostView(viewsets.ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(PostView, self).dispatch(*args, **kwargs)

    @action(detail=True, methods=['post'])
    def upvote(self, req, pk=None):
        post = Post.objects.get(pk=pk)
        post.upvotes += 1
        post.save()
        return Response({
            'id': post.id,
            'upvotes': post.upvotes
        })

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        post.downvotes += 1
        post.save()
        return Response({
            'id': post.id,
            'downvotes': post.downvotes
        })
