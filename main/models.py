from django.db import models
from django.contrib import admin

# Модель создания поста
class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
#Сортировка
    def sort_post(posts, sort_criteries):
        if sort_criteries == 'title':
            sorted_posts = sorted(posts, key=lambda post: post.title)
        elif sort_criteries == 'date':
            sorted_posts = sorted(posts, key=lambda post: post.created_date)
        else:
            sorted_posts = posts
        return sorted_posts

    #Этот класс отвечает за сортировку в админке и изменение названия модели (verbose_name_plural чтобы не было доп. буквы в конце)
    class Meta:
        verbose_name = 'Записи'
        verbose_name_plural = 'Записи'
        ordering = ['-created_date']