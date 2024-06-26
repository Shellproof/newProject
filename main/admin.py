from django.contrib import admin
from .models import *

class PostsAdmin(admin.ModelAdmin):
   search_fields = ['title']


admin.site.register(Posts)