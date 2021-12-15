from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)


    def __str__(self) -> str:
        return self.name


    def get_url(self):
        return f'/blog/category/{self.slug}/'


    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    class Meta:
        verbose_name_plural = 'Categories'

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    img = models.ImageField(upload_to = 'blog/images/%Y/%m/%d/', blank = True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank= True)
    def __str__(self) -> str:
        return f'[{self.pk}]{self.title}'


    def get_url(self):
        return f'/blog/{self.pk}/' 


    def get_absolute_url(self):
        return f'/blog/{self.pk}/' 

    