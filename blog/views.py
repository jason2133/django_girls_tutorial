# from django.shortcuts import render
# from django.utils import timezone
# from .models import Post

# # from . (from 다음에 있는 마침표 .)은 현재 디렉토리, 애플리케이션을 의미함!

# # Create your views here.

# # Django 뷰 만들기!

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {})

# C:/Users/jason/Desktop/myweb2/myweb3/blog/templates/blog/post_list.html

from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    


