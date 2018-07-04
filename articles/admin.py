from django.contrib import admin
from articles.models import Article , Category
# Register your models here.

class ArticleAdminConfig(admin.ModelAdmin):
	prepopulated_fields= {'slug': ('title',)}
	list_display = ['title', 'created_at', 'slug']
	search_fields =['title','slug','content']


class CategoryAdminConfig(admin.ModelAdmin):
	list_display = ['name', 'created_at']
	search_fields =['name','description']


admin.site.register(Article, ArticleAdminConfig)
admin.site.register(Category, CategoryAdminConfig)