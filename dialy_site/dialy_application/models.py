from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse
# Create your models here.

#Модель для поста с игрой
class Post(models.Model):
    title = models.CharField(max_length=255)# название
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL",null=True)#в настройках админки прописать зависимость от заголовка
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")# Картинка.Вродь прописал путь хранения в настройках
    content = models.TextField(blank=True)# описсание
    time_create = models.DateTimeField(auto_now_add=True)# дата создания
    time_update = models.DateTimeField(auto_now=True)# дата обновления
    torrent = models.FileField(upload_to="torrents/%Y/%m/%d/",validators=[FileExtensionValidator(['torrent'])])#если позвалять грузить кому угодно без валидации файлов создает дыры
    cat = models.ForeignKey('Category',on_delete=models.PROTECT,null=True)#Связываем таблицу с таблицей категории

    def __str__(self):
        return self.title# Выводим название при обращении

    def get_absolute_url(self):
        return reverse('post', kwargs={"post_slug":self.slug})# при обращении через модель.get_absolute_url будет возвращать ссылку со слагом

    class Meta:
        ordering = ['time_create', 'title']


class Category(models.Model):

    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat', kwargs={"cat_slug": self.slug})

