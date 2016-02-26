from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin  #<== added esv


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(
        Post,
        blank=True,
        related_name='categories'
    )
    class Meta: #<== added esv
        verbose_name_plural = "categories"  #<== added esv

    def __str__(self):
        return self.name

# class CategoryInline(admin.TabularInline):
#     model = Category

# class PostAdmin(admin.ModelAdmin):
#     inlines = [
#         CategoryInline,
#     ]

class PostInline(admin.TabularInline):
    model = Post

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]