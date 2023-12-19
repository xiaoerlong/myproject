from django.shortcuts import render

# Create your views here.
# 主页
def index(request):
    context = {
        'name': 'index'
    }
    return render(request, 'index.html', context)

# 简介
def resume(request):
    context = {
        'name': 'resume'
    }
    return render(request, 'resume.html', context)

# 工作经历
def works(request):
    context = {
        'name': 'works'
    }
    return render(request, 'works.html', context)

# 博客
def blog(request):
    context = {
        'name': 'index'
    }
    return render(request, 'blog.html', context)

# 联系
def contact(request):
    context = {
        'name': 'contact'
    }
    return render(request, 'contact.html', context)