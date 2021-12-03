from django.shortcuts import render
from .models import Post
# from django.views.generic import ListView
# from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('pk')
    return render(
        request,
        'blog/index.html',
        {
            'post' : posts,
        }
    )
