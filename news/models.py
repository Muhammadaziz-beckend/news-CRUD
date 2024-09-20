from django.db import models


class DataAddDataNowMixin(models.Model):

    data_add = models.DateField('дата добавления',auto_now_add=True)
    data_now = models.DateField('дата изменения',auto_now=True)

    class Meta:
        abstract = True

class News(DataAddDataNowMixin):
    name = models.CharField('название',max_length=35)
    decrypt = models.CharField('описания',max_length=100)
    content = models.TextField("Контент",)
    tags = models.ManyToManyField('Tag',related_name='tags',verbose_name='Теги')
    category = models.ForeignKey('Category',models.CASCADE,related_name='category')
    is_public = models.BooleanField('публичный',default=True)

    class Meat:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Tag(DataAddDataNowMixin):
    name = models.CharField(("названия"), max_length=50)

    class Meat:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(DataAddDataNowMixin):
    name = models.CharField(("названия"), max_length=50)

    class Meat:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


