from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume', views.resume, name='resume'),
    path('works', views.works, name='works'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('test', views.test_static, name='test_static'),

]