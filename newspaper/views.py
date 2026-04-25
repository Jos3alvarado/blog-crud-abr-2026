from django.views.generic import ListView
from .models import article

# Create your views here.
class ArticleListView(ListView):
    model = article
    template_name = 'article-list.html'