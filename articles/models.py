from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
class Category(models.Model):
	created_at = models.DateTimeField(default=timezone.now, editable=False)
	name = models.CharField(max_length=100)
	description =models.TextField(blank=True)

	def __str__(self):
		return '{}: {}'.format(self.created_at.strftime('%Y-%m-%d %H:%M:%S'), self.name)

	class Meta:
		ordering = ['-created_at']
		

class Article(models.Model):
    category = models.ForeignKey(Category, related_name='category' , on_delete='cascade')
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=120, unique=True, blank=True)
    content = models.TextField(blank=True, default='')
    article_file =models.FileField(blank=True)


    def __str__(self):
        return '{}: {}'.format(self.created_at.strftime('%Y-%m-%d %H:%M:%S'), self.title)

    class Meta:
        ordering = ['-created_at']


