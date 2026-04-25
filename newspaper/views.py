from django.views.generic import ListView, DetailView
from .models import article

# Create your views here.
class ArticleListView(ListView):
    model = article
    template_name = 'article-list.html'

class ArticleDetailView(DetailView):
    model = article
    template_name = 'article-detail.html'