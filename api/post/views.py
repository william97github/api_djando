from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()