from django.conf.urls import url
from first_app import views

# template tagging
app_name = 'first_app'

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^users/', views.users, name='users'),
  url(r'^registration/', views.registration, name='registration'),
  url(r'^login/', views.login_user, name='login_user'),
  url(r'^logout_user/', views.logout_user, name='logout_user'),
]
