import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RSS_GRABBER.settings')
django.setup()
from celery import Celery
from datetime import datetime
from main.models import Rss, News
import requests
from bs4 import BeautifulSoup


app = Celery('tasks', broker='redis://localhost:6379')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        10.0,      # run every 10 minutes
        update_news_priodically.s(),
        name='update_news')


@app.task(queue='news')
def update_news_priodically():
    print(f'-----------task started at {datetime.utcnow()}-----------')

    rss_list = Rss.objects.all()

    for rss in rss_list:
        response = requests.get(rss.link)
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')

        existing_news_titles = News.objects.values_list('title', flat=True)
        for item in items:
            title = item.title.text
            if title in existing_news_titles:
                continue
            link = item.link.text
            description = item.description.text
            author = item.author.text
            publish_date = datetime.strptime(item.pubDate.text,'%d %b %Y %H:%M:%S %z').replace(tzinfo=None)

            News.objects.create(title=title, link=link, description=description, author=author, publish_date=publish_date)
    print('------------------------task ended-------------------------')
