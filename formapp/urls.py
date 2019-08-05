from django.conf.urls import url
from formapp import views

urlpatterns=[

    url(r'^hello-form$',views.userProfile)

]