from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('articulos/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
]