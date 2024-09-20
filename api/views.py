from rest_framework.generics import (
    ListAPIView,
    GenericAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from rest_framework.mixins import (
    ListModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
)
from rest_framework.response import Response
from news.models import *
from .serializer import NewsSerializer, TagsSerializer, CategorySerializer
from .pgintion import SimplePagintion


class ListCreateNews(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = "id"
    pagination_class = SimplePagintion

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class ListUpdateDeleteNews(RetrieveUpdateDestroyAPIView):
    queryset = News.objects
    serializer_class = NewsSerializer
    lookup_field = "id"


class ListCreateTeg(ListModelMixin, CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListUpdateDeleteTeg(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects
    serializer_class = TagsSerializer
    lookup_field = "id"


class ListCreateCategory(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListUpdateDeleteCategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects
    serializer_class = TagsSerializer
    lookup_field = "id"
