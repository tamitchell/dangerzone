from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^$', views.news_list, name="news_list"),
    url(r'^animals$', views.animal_list, name="animal_list")
]