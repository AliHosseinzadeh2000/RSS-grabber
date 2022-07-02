import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RSS_GRABBER.settings')
django.setup()
from celery import Celery
from datetime import datetime
from main.models import Rss, News
import requests
from bs4 import BeautifulSoup


def get_rss_items(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'xml')    
    return soup.find_all('item')


def get_items_list(items):

    items_list = []
    existing_news_titles = News.objects.values_list('title', flat=True)

    for item in items:
        if item and item.title and item.link and item.description and item.author and item.pubDate:
            if item.title.text not in existing_news_titles:

                new = News(
                        title=item.title.text,
                        link=item.link.text,
                        description=item.description.text,
                        author=item.author.text,
                        publish_date=datetime.strptime(item.pubDate.text,'%d %b %Y %H:%M:%S %z')
                        )
                items_list.append(new)
    return items_list
    

app = Celery('tasks', broker='redis://localhost:6379')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        3600.0,      # run every hour
        update_news_periodically.s(),
        name='update_news')


@app.task(queue='news')
def update_news_periodically():

    print(f'-----------task started at {datetime.utcnow()}-----------')

    rss_list = Rss.objects.all()

    for rss in rss_list:
        items = get_rss_items(rss.link)
        items_list = get_items_list(items)
        News.objects.bulk_create(items_list) 

    print('------------------------task ended-------------------------')
