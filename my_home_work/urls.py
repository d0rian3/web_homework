from django.urls import path, include, re_path
from myapp.views import main, my_feed, create,profile,register,set_password,login,logout,data_sort


urlpatterns = [
    path('', main, name="main"),
    path('my-feed/', my_feed, name="my_feed"),
    path('<int:article_id>/', include('myapp.urls_article')),
    path('topics/', include('myapp.urls_topics')),
    path('create/', create, name="create"),
    path('profile/', profile, name="profile"),
    path('register/', register, name="register"),
    path('set_password/', set_password, name="set_password"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    re_path(r'^(?P<year>[1-9]\d{3})/(?P<month>0[1-9]|1[0-2])/$', data_sort, name="data_sort"),
]
