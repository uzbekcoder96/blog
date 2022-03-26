from django.shortcuts import render
from .models import Post


def home_page_view(request):
    posts = Post.objects.all()

    context = {'posts':posts}
    return render(request, 'base.html', context)



def post_detail_view(request, id):

    post = Post.objects.get(id=id)
    context = {'post':post}
    return render(request, 'post-details.html', context)





def all_post_view(request):
    posts = Post.objects.all()

    context = {'posts':posts}
    return render(request, 'blog.html', context)




def about_view(request):

    context = {}
    return render(request, 'about.html', context)





def contact_view(request):

    context = {}
    return render(request, 'contact.html', context)        