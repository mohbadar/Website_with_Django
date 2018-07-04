from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=120)
	contact = models.CharField(max_length=120)
	message = models.TextField()
	created_at = models.DateTimeField(default=timezone.now, editable=False)


	def __str__(self):
		return '{}: {} : {}'.format(self.created_at.strftime('%Y-%m-%d %H:%M:%S'), self.name, self.contact)

	class Meta:
		ordering = ['-created_at']
        


