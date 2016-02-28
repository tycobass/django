from django.contrib import admin
from django.db import models   #<== added esv

from myblog.models import Category
from myblog.models import Post



admin.site.register(Category)
# admin.site.register(Post) #<== commented to support inline esv

class CategoryInline(admin.TabularInline):  #<== added esv
    model = Category.posts.through
    #model = models.ManyToManyField(Category)
    # categories = models.ManyToManyField(Category)  #<== added esv
    # model = categories  #<== added esv

class PostAdmin(admin.ModelAdmin):  #<== added esv
    inlines = [
        CategoryInline,
    ]

# class PostInline(admin.TabularInline):  #<== added esv
#     model = Post

# class CategoryInline(admin.ModelAdmin):  #<== added esv
#     inlines = [
#         PostInline
#     ]

admin.site.register(Post, PostAdmin) #<== commented to support inline esv