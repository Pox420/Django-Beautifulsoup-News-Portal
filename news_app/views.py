from django.shortcuts import render

from news_app.models import NewsPortal
from . import soup
from user.forms import UserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    for i in soup.page_details:
        title = i['title']
        image_link = i['image_link']
        sub_title = i['sub_title']
        main_content = i['main_content']

        if NewsPortal.objects.filter(title=title).exists():
            pass
        else:
            NewsPortal.objects.create(title=title, image_link=image_link, sub_title=sub_title, main_content=main_content)

    news = NewsPortal.objects.all().order_by('-id')

    context = {
        'news':news,
    }
    return render(request, 'news_app/index.html',context=context)

@login_required(login_url='/accounts/login/')
def detail_page(request, id):
    news = NewsPortal.objects.get(id=id)
    form = UserForm()

    context = {
        'news':news,
        'form':form,
    }
    return render(request, 'news_app/details.html',context=context)
