from django.urls import path

from .views import *

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('cat/<slug:cat_slug>',Sowe_cat.as_view(),name='cat'),
]

