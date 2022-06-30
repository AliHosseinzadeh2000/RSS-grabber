from django.urls import path
from main.views import NewsListView


urlpatterns = [
    path('news-list/', NewsListView.as_view()),
]
