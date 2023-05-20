from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from django.views.generic import ListView,DetailView
from .utils import *

from .models import *


class Home(DataMixin,ListView):
    model = Post# выбираем все записи из базы постов
    template_name = "directory.html"# какой шаблон вызывать
    context_object_name = "post"#Записать по какому имени будем вызывать объект подефолту object_list

    def get_context_data(self, *, object_list=None, **kwargs): # Вызывается автоматом
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ShowPost(DetailView):
    model = Post
    template_name = "show_post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = 'post'

class Sowe_cat(DataMixin,ListView):
    model = Post# выбираем все записи из базы постов
    template_name = "directory.html"# какой шаблон вызывать
    context_object_name = "post"#Записать по какому имени будем вызывать объект подефолту object_list

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs): # Вызывается автоматом
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

