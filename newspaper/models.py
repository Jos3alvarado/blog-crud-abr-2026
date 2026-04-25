from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', 
                                on_delete=models.CASCADE
                                )
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title