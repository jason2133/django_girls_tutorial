from django.shortcuts import render

# Create your views here.

# Django 뷰 만들기!

def post_list(request):
    return render(request, 'blog/post_list.html', {})

# C:/Users/jason/Desktop/myweb2/myweb3/blog/templates/blog/post_list.html


