from django.shortcuts import render
from home_slider.models import home_slider ,skills
from Tags.models import Blog ,Blog_Header
from django.core.paginator import Paginator
from projects.models import Project, ProjectImage, Category ,Project_Header 
from collections import defaultdict
from django.db.models import Prefetch
from social.models import socail_media , social_header
from collections import defaultdict
from education.models import Education
from header.models import cv, SiteSettings



def home(request):
    main_slide = home_slider.objects.all()[0:1]
    all_blogs = Blog.objects.all().order_by('-created_at')[0:3]
    skills_data = skills.objects.all()
    data_category = Category.objects.all()
    project_header = Project_Header.objects.all()
    blogs_header = Blog_Header.objects.all()
    all_education = Education.objects.all()

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
        'proj_header':project_header,
        'objc_header':blogs_header,
        'all_educa':all_education,
    }

    return render(request, 'index.html', context)


def blogs(request):
    
    all_blogs = Blog.objects.all().order_by('-created_at')  # latest blog first
    data={
        'blogs':all_blogs
    }
    return render(request, 'blog.html', data)


def blog_detail(request ,slug):
    # blogs_slugs = Blog.objects.get(slugs=slug)
    blogs_slugs = Blog.objects.filter(slugs=slug)  
    socila_all = socail_media.objects.all()
    social_head = social_header.objects.all()
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
        'soc_all':socila_all,
        'soci_head':social_head,
    }
    return render(request, 'blog_detail.html', data)


def project(request):
    
    data_category = Category.objects.all()
    project_header = Project_Header.objects.all()
    blogs_header = Blog_Header.objects.all()
    

    # Create a dictionary: category_id => list of projects
    category_projects = defaultdict(list)
    all_projects = Project.objects.select_related('category').prefetch_related('images')
    
    for proj in all_projects:
        category_projects[proj.category.id].append(proj)
    

    context = {
        'category': data_category,
        'category_projects': category_projects,
        'proj_header':project_header,
        'objc_header':blogs_header,
    }
    return render(request, 'projects.html',context)


def project_detail(request ,pslug):
    project_slugs = Project.objects.get(auto_slug = pslug)
    project_slugs = Project.objects.filter(auto_slug = pslug)  
    socila_all = socail_media.objects.all()
    social_head = social_header.objects.all()
    all_project = Project.objects.all().order_by('-created_at')  # latest blog first
    if not project_slugs.exists():
        return render(request, '404.html')
    current_blog = project_slugs.first()


    # Implement next and previous blog logic
    next_project = Project.objects.filter(created_at__gt=current_blog.created_at).order_by('created_at').first()
    previous_project = Project.objects.filter(created_at__lt=current_blog.created_at).order_by('-created_at').first()

    data = {
        'sl': project_slugs,                   # This will contain the current blog (as a queryset)
        'sideprojects': all_project,                  # All blogs
        'servicedatafinal': all_project,       # Keeping this name, though not paginated
        'next_blog': next_project,
        'previous_blog': previous_project,
        'soc_all':socila_all,
        'soci_head':social_head,
    }

    return render(request, 'project_detail.html', data)









