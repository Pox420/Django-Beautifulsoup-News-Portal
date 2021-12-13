from django.shortcuts import render

from news_app.models import NewsPortal
from . import soup

# Create your views here.
def index(request):
    for i in soup.page_details:
        title = i['title']
        image_link = i['image_link']
        sub_title = i['sub_title']
        main_content = i['main_content']

        if NewsPortal.objects.filter(title=title).exists():
            print('exists')
        else:
            NewsPortal.objects.create(title=title, image_link=image_link, sub_title=sub_title, main_content=main_content)

    news = NewsPortal.objects.all()

    context = {
        'news':news,
    }
    return render(request, 'news_app/index.html',context=context)

def detail_page(request):
    # context = {
    #     'soup':soup.page_details
    # }
    # return render(request, 'news_app/detail_page.html',context=context)
    pass
