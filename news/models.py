from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
CONDITIONS = (
    (0, 'Announcement'),
    (1, 'News'),
    (2, 'Post'),
)


class News(models.Model):
    # user = models.ForeignKey(User, related_name='news' , on_delete='cascade')
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    news_type = models.IntegerField(choices=CONDITIONS)
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=120, unique=True, blank=True)
    content = models.TextField(blank=True, default='')
    new_file =models.FileField(blank=True)


    def __str__(self):
        return '{}: {}'.format(self.created_at.strftime('%Y-%m-%d %H:%M:%S'), self.title)

    class Meta:
        ordering = ['-created_at']
