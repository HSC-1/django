from django.contrib import admin
from .models import Post, Category
# Register your models here.


admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_filed={'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)