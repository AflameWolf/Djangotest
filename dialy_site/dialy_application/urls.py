from django.urls import path

from .views import *

urlpatterns = [
    path('',Home.as_view(), name='home'),#главный путь ссылаеться на класс представления который будет открывать домашнюю страницу
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('cat/<slug:cat_slug>',Sowe_cat.as_view(),name='cat'),
]

