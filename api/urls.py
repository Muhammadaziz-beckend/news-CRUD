from django.urls import path, include
from .views import (
    ListCreateNews,
    ListCreateTeg,
    ListCreateCategory,
    ListUpdateDeleteNews,
    ListUpdateDeleteTeg,
    ListUpdateDeleteCategory,
)


urlpatterns = [
    path("news/", ListCreateNews.as_view()),
    path("news/<int:id>", ListUpdateDeleteNews.as_view()),
    path("teg/", ListCreateTeg.as_view()),
    path("teg/<int:id>", ListUpdateDeleteTeg.as_view()),
    path("category/", ListCreateCategory.as_view()),
    path("category/<int:id>", ListUpdateDeleteCategory.as_view()),
]
