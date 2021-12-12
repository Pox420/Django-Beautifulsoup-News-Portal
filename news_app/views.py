from django.shortcuts import render
from . import soup

# Create your views here.
def index(request):
    context = {
        'soup':soup.soup
    }
    return render(request, 'news_app/index.html',context=context)