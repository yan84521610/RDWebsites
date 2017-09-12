from django.shortcuts import get_object_or_404, render

from .models import News


def news(request):
    news_list = News.published.all()
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
        'main/news_detail.html',
        {'news': news},
    )

def index(request):
    return render(request, 'main/index.html', )

def about(request):
    return render(request, 'main/about.html', )

def products(request):
    return render(request, 'main/products.html', )

def hr(request):
    return render(request, 'main/hr.html', )

def contacts(request):
    return render(request, 'main/contacts.html', )