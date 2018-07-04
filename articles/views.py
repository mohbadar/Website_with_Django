from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from articles.models import Article


# Create your views here.

def articles(request):
	article_list = Article.objects.all()
	page = request.GET.get('page',1)

	paginator = Paginator(article_list,2)

	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request,'research/article.html', {'articles': articles})

def article_detail(request, slug):

	article = Article.objects.get(slug=slug)
	return render(request, 'research/article_detail.html',{'article':article})