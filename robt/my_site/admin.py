from .models import Blog, Call
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    list_display_link = ['title']
    search_fields = ['title']

admin.site.register(Blog)

admin.site.register(Call)





