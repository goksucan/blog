from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category

def index(request):
    category = Category.objects.all
    return render(request, 'core/index.html',  {'categories': category})

def post_detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug = slug )
    category = Category.objects.all
    return render (request, 'core/detail.html', {'post': post, 'categories':category})

def category(request, slug):
    categori = get_object_or_404(Category, slug = slug)
    category = Category.objects.all
    return render (request, 'core/category.html', {'category':categori, 'categories': category})

def tag(request, tag):
     posts = Post.objects.filter(tags__name=tag)
     return render(request, 'core/tag.html', {'tag': tag, 'posts': posts})


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse ("\n".join(text), content_type="text/plain")