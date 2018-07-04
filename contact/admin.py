from django.contrib import admin
from contact.models import Contact

class ContactAdminConfig(admin.ModelAdmin):
	list_display = ['name', 'created_at', 'contact']
	search_fields =['name','contact','message']

admin.site.register(Contact,ContactAdminConfig)
