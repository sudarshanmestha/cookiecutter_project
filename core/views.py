from django.shortcuts import render

from blog.models import Post, Category

def frontpage(request):

    return render(request, 'core/frontpage.html')

def blog(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'core/blog.html', {'posts': posts})


def about(request):
    return render(request, 'core/about.html')