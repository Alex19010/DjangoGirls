from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.publish.all()
    return render(request, 'blog\post\list.html', {'posts': posts})

def post_detail(request):
    post = get_object_or_404(
        id=id,
        status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post}
    )
