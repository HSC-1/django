from django.contrib import admin
from .models import Comment, Post, Category
# Register your models here.


admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_filed={'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
