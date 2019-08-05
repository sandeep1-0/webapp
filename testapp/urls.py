from django.conf.urls import url
from testapp import views

urlpatterns=[
    url(r'^hello-django$',views.helloDjango),
    url(r'^hello-python$',views.helloPython)
]

