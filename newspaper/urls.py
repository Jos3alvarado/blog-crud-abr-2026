from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('articulos/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('articulo/crear/', views.ArticleCreateView.as_view(), name='article-create'),
    path('articulo/<int:pk>/editar/', views.ArticleUpdateView.as_view(), name='article-update'),

]