from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from django.utils import timezone ## added this in
from blog.serializers import PostSerializer
from blog.models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#we want published blog posts sorted by published_date
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})