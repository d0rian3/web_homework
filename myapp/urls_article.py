from django.urls import path
from .views import article, article_comment, article_delete, article_update

urlpatterns = [
    path('', article, name='article'),
    path('comment', article_comment, name='article_comment'),
    path('update', article_update, name='article_update'),
    path('delete', article_delete, name='article_delete'),
]

