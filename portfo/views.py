from django.shortcuts import render
from home_slider.models import home_slider ,skills
from Tags.models import Blog
from django.core.paginator import Paginator
from projects.models import Project, ProjectImage, Category
from collections import defaultdict



from collections import defaultdict

def home(request):
    main_slide = home_slider.objects.all()[0:1]
    all_blogs = Blog.objects.all().order_by('-created_at')[0:3]
    skills_data = skills.objects.all()
    data_category = Category.objects.all()

    # Create a dictionary: category_id => list of projects
    category_projects = defaultdict(list)
    all_projects = Project.objects.select_related('category').prefetch_related('images')

    for proj in all_projects:
        category_projects[proj.category.id].append(proj)

    context = {
        'sld': main_slide,
        'blogs': all_blogs,
        'skil_data': skills_data,
        'category': data_category,
        'category_projects': category_projects,
    }

    return render(request, 'index.html', context)





def blog_detail(request ,slug):
    # blogs_slugs = Blog.objects.get(slugs=slug)
    blogs_slugs = Blog.objects.filter(slugs=slug)  
    all_blogs = Blog.objects.all().order_by('-created_at')  # latest blog first
    if not blogs_slugs.exists():
        return render(request, '404.html')
    current_blog = blogs_slugs.first()

    # Get all blogs to use elsewhere if needed
    all_blogs = Blog.objects.all().order_by('-created_at')

    # Implement next and previous blog logic
    next_blog = Blog.objects.filter(created_at__gt=current_blog.created_at).order_by('created_at').first()
    previous_blog = Blog.objects.filter(created_at__lt=current_blog.created_at).order_by('-created_at').first()

    data = {
        'sl': blogs_slugs,                   # This will contain the current blog (as a queryset)
        'blogs': all_blogs,                  # All blogs
        'servicedatafinal': all_blogs,       # Keeping this name, though not paginated
        'next_blog': next_blog,
        'previous_blog': previous_blog,
    }
    return render(request, 'blog_detail.html', data)

def project_detail(request ,slug):
    # blogs_slugs = Blog.objects.get(slugs=slug)
    blogs_slugs = Blog.objects.filter(slugs=slug)  
    all_blogs = Blog.objects.all().order_by('-created_at')  # latest blog first
    if not blogs_slugs.exists():
        return render(request, '404.html')
    current_blog = blogs_slugs.first()

    # Get all blogs to use elsewhere if needed
    all_blogs = Blog.objects.all().order_by('-created_at')

    # Implement next and previous blog logic
    next_blog = Blog.objects.filter(created_at__gt=current_blog.created_at).order_by('created_at').first()
    previous_blog = Blog.objects.filter(created_at__lt=current_blog.created_at).order_by('-created_at').first()

    data = {
        'sl': blogs_slugs,                   # This will contain the current blog (as a queryset)
        'blogs': all_blogs,                  # All blogs
        'servicedatafinal': all_blogs,       # Keeping this name, though not paginated
        'next_blog': next_blog,
        'previous_blog': previous_blog,
    }
    return render(request, 'blog_detail.html', data)


def blogs(request):
    all_blogs = Blog.objects.all().order_by('-created_at')  # latest blog first
    data={
        'blogs':all_blogs
    }
    return render(request, 'blog.html', data)



def project(request,pk):

    all_blogs = Blog.objects.all().order_by('-created_at')  # latest blog first
    data={
        'blogs':all_blogs
    }
    return render(request, 'projects.html',data)
