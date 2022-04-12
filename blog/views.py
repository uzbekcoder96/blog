from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required(login_url='users/login/')
def home_page_view(request):
    posts = Post.objects.all()

    context = {'posts':posts}
    return render(request, 'base.html', context)


@login_required(login_url='users/login/')
def post_detail_view(request, id):

    post = Post.objects.get(id=id)
    context = {'post':post}
    return render(request, 'post-details.html', context)




@login_required(login_url='users/login/')
def all_post_view(request):
    posts = Post.objects.all()

    context = {'posts':posts}
    return render(request, 'blog.html', context)



@login_required(login_url='users/login/')
def about_view(request):

    context = {}
    return render(request, 'about.html', context)

@login_required(login_url='users/login/')
def contact_view(request):

    context = {}
    return render(request, 'contact.html', context)        




