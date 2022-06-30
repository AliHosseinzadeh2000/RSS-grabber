from rest_framework import mixins
from rest_framework import generics
from main.models import News
from main.serializers import NewsListSerializer


class NewsListView(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = News.objects.all()
    serializer_class = NewsListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
