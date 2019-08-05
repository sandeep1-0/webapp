from django.conf.urls import url
from crud import views

urlpatterns = [

    url(r'^create$',views.create),
    url(r'^update$',views.update),
    url(r'^index$',views.index),
    url(r'^delete$',views.delete),
    url(r'^view$',views.view)
]