from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.db.models import Q

from .models import Post, Tag
# Create your views here.
def posts_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query) | Q(company__icontains=search_query))
    else:
        posts = Post.objects.all()

    return render(request, 'blog/index.html', context={'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})

def aboutUs(request):
    return render(request, 'blog/AboutUs.html')

def home(request):
    return render(request, 'app1/main.html')