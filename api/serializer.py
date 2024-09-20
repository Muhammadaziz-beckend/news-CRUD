from rest_framework.serializers import ModelSerializer
from news.models import News, Tag,Category


class NewsSerializer(ModelSerializer):

    class Meta:
        model = News
        fields = "__all__"


class TagsSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'