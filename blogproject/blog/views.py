from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def index(request):
    articles = Article.objects.all().order_by('time')
    return render(request,'blog/index.html',context={
        'title':'blog home page',
        'article':articles,
    })
def articles_page(request,article_id):
    article = Article.objects.get(pk=article_id)
    return render(request,'blog/article.html',context={
        'title':article.title,
        'body':article.context,
        'author':article.author,
        'time':article.time
    })

def edit_page(request):
    return render(request,'blog/edit_page.html')

def edit_action(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('context','CONTEXT')
    Article.objects.create(title=title,context=content)
    articles = Article.objects.all()
    return render(request, 'blog/article.html', context={
        'article': articles,
    })
