from . import views
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    path('', views.index),
    path('article/<int:article_id>',views.articles_page),
    path('edit',views.edit_page),
    path('edit/action',views.edit_action,name='edit_action')
]