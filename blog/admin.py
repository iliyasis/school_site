from django.contrib import admin
from blog.models import *
# Register your models here.
class BlogCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogCategory, BlogCategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost, PostAdmin)