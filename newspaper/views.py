from django.views.generic import (
                                ListView,
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView
                                )
from .models import article
from django.urls import reverse_lazy

# Create your views here.
class ArticleListView(ListView):
    model = article
    template_name = 'article-list.html'

class ArticleDetailView(DetailView):
    model = article
    template_name = 'article-detail.html'

class ArticleCreateView(CreateView):
    model = article
    template_name = 'article-create.html'
    fields = ['title', 'author', 'content']

class ArticleUpdateView(UpdateView):
    model = article
    template_name = 'article-update.html'
    fields = ['title', 'content']

class ArticleDeleteView(DeleteView):
    model = article
    template_name = 'article-delete.html'
    success_url = reverse_lazy('article_list')