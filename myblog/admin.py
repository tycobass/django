from django.contrib import admin
from django.db import models   #<== added esv

from myblog.models import Category
from myblog.models import Post



admin.site.register(Category)
# admin.site.register(Post) #<== commented to support inline esv

class CategoryInline(admin.TabularInline):  #<== added esv
    model = Category.posts.through  #<== posts.through added esv


class PostAdmin(admin.ModelAdmin):  #<== added esv
    inlines = [
        CategoryInline,
    ]
    exclude = ('posts',)


admin.site.register(Post, PostAdmin) #<== commented to support inline esv