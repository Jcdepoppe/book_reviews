from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^add$', views.add_book, name='add'),
    url(r'^(?P<num>\d+)$', views.book, name='book'),
    url(r'^new$', views.new_book, name='new'),
    url(r'^review$', views.add_review, name='review'),
]