from django.urls import path, include, re_path
from myapp.views import main, my_feed, create,profile,register,set_password,login,logout,data_sort


urlpatterns = [
    path('/', main),
    path('/my-feed/', my_feed),
    path('article/', include('myapp.urls')),
    path('topics/', include('myapp.urls')),
    path('create/', create),
    path('profile/', profile),
    path('register/', register),
    path('set_password/', set_password),
    path('login/', login),
    path('logout/', logout),
    re_path(r'^(?P<year>[1-9]\d{3})/(?P<month>0[1-9]|1[0-2])/$', data_sort),
]
