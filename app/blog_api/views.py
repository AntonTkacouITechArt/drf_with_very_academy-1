from rest_framework import generics

from blog.models import Post
from blog_api.serializers import PostSerializer


class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetailAPI(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

