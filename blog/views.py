from django.shortcuts import render, get_object_or_404
from .models import Blog 

# Create your views here.
def all_blogs(request):
    #blog_count = Blog.objects.counts
    blogs = Blog. objects.order_by('-data')
    return render(request, 'blog/all_bogs.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog = get_objets_or404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog' : blog})