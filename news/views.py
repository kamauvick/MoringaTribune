import datetime as dt

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from .models import Article


# Create your views here.
def welcome(request):
    articles = Article.query()
    params = {
        'articles': articles
    }
    return render(request, 'welcome.html', params)


def error(request):
    return HttpResponse('This is an error page')


def past_day_news(request, past_date):
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        raise Http404
        # assert False

    if date == dt.date.today():
        return redirect(news_today)
    news = Article.days_news(date)
    params = {
        'date': date,
        'news': news,
    }
    return render(request, 'all_news/past_news.html', params)


def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    params = {
        'date': date,
        'news': news,
    }
    return render(request, 'all_news/today_news.html', params)


def search_results(request):
    if 'article' in request.GET and request.GET['article']:
        search_term = request.GET.get('article')
        searched_articles = Article.search(search_term)
        print(searched_articles)
        message = f'{search_term}'
        params = {
            'searched_articles': searched_articles,
            'message': message,
        }
        return render(request, 'all_news/search.html', params)
    else:
        message = 'You haven\'t provided a search term yet'
        params = {
            'message': message,
        }
        return render(request, 'all_news/search.html', params)


class DoesNotExist(object):
    pass


def article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all_news/article.html", {"article": article})
