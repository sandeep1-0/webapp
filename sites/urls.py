from django.conf.urls import url
from sites import views

urlpatterns=[
    url(r'^login$',views.login),
    url(r'^registration$',views.registration),
    url('^$',views.dashBoard),
    url(r'^logout$',views.logout),
    url(r'^test_page$',views.static_page)
]