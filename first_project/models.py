from django.db import models
from django.shortcuts import render

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    img = models.ImageField(upload_to = 'blog/images/%Y/%m/%d/', blank = True)

    def __str__(self) -> str:
        return f'[{self.pk}]{self.title}'


    def get_url(self):
        return f'/blog/{self.pk}/' 