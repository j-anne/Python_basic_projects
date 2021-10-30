from django.conf.urls import url
from first_project import views

urlpatterns = [
    url(r'$', views.index, name='index'),
    url(r'$', views.fakeInfo, name='fakeInfo')
]