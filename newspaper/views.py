from django.views.generic import (
                                ListView,
                                DetailView,
                                CreateView,
                                UpdateView
                                )
from .models import article

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