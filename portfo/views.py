from django.shortcuts import render
from home_slider.models import home_slider
from Tags.models import Blog


def home(request):
    main_slide = home_slider.objects.all()[0:1]
    all_blogs = Blog.objects.all().order_by('-created_at')[0:4]  # latest blog first

    data = {
        'sld': main_slide,
        'blogs': all_blogs
    }

    return render(request, 'index.html', data)

def blog_detail(request ,slug):
    # blogs_slugs = Blog.objects.get(slugs=slug)
    blogs_slugs = Blog.objects.filter(slugs=slug)  
    all_blogs = Blog.objects.all().order_by('-created_at')  # latest blog first

    data = {
        'sl':blogs_slugs,
        'blogs': all_blogs,
    }
    return render(request, 'blog_detail.html' ,data)

def blogs(request):
    all_blogs = Blog.objects.all().order_by('-created_at')  # latest blog first
    data={
        'blogs':all_blogs
    }
    return render(request, 'blog.html', data)

def project(request):
    
    all_blogs = Blog.objects.all().order_by('-created_at')  # latest blog first
    data={
        'blogs':all_blogs
    }
    return render(request, 'projects.html',data)
