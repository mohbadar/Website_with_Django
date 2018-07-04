from django.shortcuts import render
from news.models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def news_list(request):
	news_list = News.objects.filter(news_type=1)
	page = request.GET.get('page',1)

	paginator = Paginator(news_list,2)

	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		news = paginator.page(1)
	except EmptyPage:
		news = paginator.page(paginator.num_pages)
	return render(request, 'publication/news.html' , {'news': news })


# home
def home(request):
	return render(request,'index.html')


# news_detail
def news_detail(request,slug):
	
	news = News.objects.get(slug=slug)
	return render(request,'publication/news_detail.html', {'news':news})

# get announcements
def announcement_list(request):
	news_list = News.objects.filter(news_type=0)
	page = request.GET.get('page',1)

	paginator = Paginator(news_list,2)

	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		news = paginator.page(1)
	except EmptyPage:
		news = paginator.page(paginator.num_pages)
	return render(request,'publication/news.html',{'news':news})

