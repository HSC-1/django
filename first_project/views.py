# from django.shortcuts import render
from django.db.models import fields
from django.shortcuts import get_object_or_404, render
from .models import Category, Post
from django.views.generic import ListView, DetailView, CreateView

from first_project import models
# from django.views.generic import ListView
# from .models import Post
# Create your views here.



class PostCreate(CreateView):
    model = Post
    fields = ['title','content', 'img', 'category']

class PostList(ListView):
    paginate_by = 2
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['no_category_count'] = Post.objects.filter(category=None).count()
        return context


class PostDetail(DetailView):
    model = Post


def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'first_project/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_count': Post.objects.filter(category=None).count(),
            'category':category,
        }
    )
# def index(request):
#     posts = Post.objects.al l().order_by('pk')
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts' : posts,
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk= pk)
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post' : post, 
#         }
#     )
