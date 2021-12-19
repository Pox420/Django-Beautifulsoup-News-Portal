from django.shortcuts import render

from news_app.models import NewsPortal
from .soup import page_details
from user.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    try:
        print('index started')
        for i in page_details:
            title = i['title']
            image_link = i['image_link']
            sub_title = i['sub_title']
            main_content = i['main_content']

            if NewsPortal.objects.filter(title=title).exists():
                pass
            else:
                NewsPortal.objects.create(title=title, image_link=image_link, sub_title=sub_title, main_content=main_content)
                print('created')
        user_list = NewsPortal.objects.all().order_by('-id')
        print('index ended')
        page = request.GET.get('page', 1)
        paginator = Paginator(user_list, 6)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request, 'news_app/index.html', { 'users': users })
    except Exception as e:
        news = NewsPortal.objects.all().order_by('-id')
        context = {
            'news':news,
        }
        return render(request, 'news_app/index.html',context=context)

def about(request):
    return render(request, 'news_app/about.html')


@login_required(login_url='/user/login/')
def detail_page(request, id):
    news = NewsPortal.objects.get(id=id)
    form = UserForm()

    context = {
        'news':news,
        'form':form,
    }
    return render(request, 'news_app/details.html',context=context)
