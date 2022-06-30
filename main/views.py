from rest_framework import mixins
from rest_framework import generics
from main.models import News
from main.serializers import NewsListSerializer
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 500


class NewsListView(mixins.ListModelMixin, generics.GenericAPIView):

    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
