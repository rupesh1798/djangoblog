from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
from django.shortcuts import render
def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
