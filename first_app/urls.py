from django.conf.urls import url
from first_app import views

# template tagging
app_name = 'first_app'

urlpatterns = [
  url(r'^$', views.index, name='index'),
]
