from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from contact.forms import ContactForm

def support(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			supportContact = form.save(commit = False)

			supportContact.name  = request.name
			supportContact.contact = request.contact
			supportContact.message = request.message

			supportContact.save()

			return render_to_response("static/support.html", RequestContext(request))


	else:
		form  = ContactForm()
	return render(request, 'static/support.html' , {'form':form })



def members(request):
	return render(request, 'static/member.html')

def about(request):
	return render(request, 'static/about.html')

def archicture(request):
	return render(request, 'static/archicture.html')