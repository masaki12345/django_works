from rest_framework import generics

from .models import Post
from .permissions import IsAuthorOrReadOnly  # 追加
from .serializers import PostSerializer


# ListCreateAPIView -> read-write endpoint
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# RetrieveUpdateDestoryAPIView -> ALlows read, update, delete
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # 追加
    queryset = Post.objects.all()
    serializer_class = PostSerializer
