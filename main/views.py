from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', )

def about(request):
    return render(request, 'main/about.html', )

def news(request):
    return render(request, 'main/news.html', )

def products(request):
    return render(request, 'main/products.html', )

def hr(request):
    return render(request, 'main/hr.html', )

def contacts(request):
    return render(request, 'main/contacts.html', )