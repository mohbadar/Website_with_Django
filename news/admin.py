from django.contrib import admin

# Register your models here.
from . import models

class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields= {'slug': ('title',)}
	list_display = ['title', 'news_type']
	search_fields =['title','slug','content']

admin.site.register(models.News, NewsAdmin)
