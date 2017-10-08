from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import News, Employment


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

def gongsijianjie(request):
    return render(request, 'main/gongsijianjie.html', )

def guanlituandui(request):
    return render(request, 'main/guanlituandui.html', )

def gongsirongyu(request):
    return render(request, 'main/gongsirongyu.html', )

def products(request):
    return render(request, 'main/products.html', )

def primer(request):
    return render(request, 'main/primer.html', )

def hr(request):
    object_list = News.published.filter(category='employment')
    return render(request, 'main/hr.html', {'employment_list': object_list})

def employment(request):
    object_list = Employment.published.filter(category='employment')
    paginator = Paginator(object_list, 10)  # 10 posts in each page
    page = request.GET.get('page')
    try:
        employment_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        employment_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        employment_list = paginator.page(paginator.num_pages)
    return render(
        request,
        'main/employment.html',
        {'employment_list': employment_list}
    )

def employment_detail(request, year, month, day, employment, category):
    employment = get_object_or_404(Employment, slug=employment,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             category=category)
    return render(
        request,
        "main/employment_detail.html",
        {'employment': employment},
    )

def cooperation(request):
    return render(request, 'main/cooperation.html', )

def contacts(request):
    return render(request, 'main/contacts.html', )