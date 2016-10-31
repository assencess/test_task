from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.users, name='index_page'),
    url(r'^students/$', views.students, name='students_list'),
]
