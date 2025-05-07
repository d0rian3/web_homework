from django.urls import path
from .views import topics, topic_id, topic_id_subscribe, topic_id_unsubscribe

urlpatterns = [
    path('', topics, name='topics'),
    path('<int:topic_id>/', topic_id, name='topics_id'),
    path('<int:topic_id>/topic_id_subscribe/', topic_id_subscribe, name='topic_id_subscribe'),
    path('<int:topic_id>/topic_id_unsubscribe/', topic_id_unsubscribe, name='topic_id_unsubscribe'),
]

