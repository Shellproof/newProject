from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from .models import Posts

import datetime

# Вывод хтмл страницы с постами.
def post_list(request):
    posts = Posts.objects.all()
    return render(request, 'main/post_list.html', {'posts': posts})

#Вывод функции сортировки
def posts_view(request):
    posts = Posts.objects.all()

    sort_criteria = request.GET.get('sort', '')

    sorted_posts = sort_post(posts, sort_criteria)

    context = {
        'posts': sorted_posts,
    }

    return render(request, 'posts.html', context)