from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import News


def news(request):
    object_list = News.published.filter(category='news')
    paginator = Paginator(object_list, 5)  # 5 posts in each page
    page = request.GET.get('page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        news_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        news_list = paginator.page(paginator.num_pages)
    return render(
        request,
        'main/news.html',
        {'news_list': news_list}
    )

def news_detail(request, year, month, day, news):
    news = get_object_or_404(News, slug=news,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(
        request,
        "main/news_detail.html",
        {'news': news},
    )

def index(request):
    return render(request, 'main/index.html', )

def about(request):
    return render(request, 'main/about.html', )

def products(request):
    return render(request, 'main/products.html', )

def hr(request):
    object_list = News.published.filter(category='employment')
    return render(request, 'main/hr.html', {'employment_list': object_list})

def cooperation(request):
    return render(request, 'main/cooperation.html', )

def contacts(request):
    return render(request, 'main/contacts.html', )