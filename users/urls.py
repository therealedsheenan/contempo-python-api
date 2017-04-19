from django.conf.urls import url
from users import views

# template tagging
app_name = 'users'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^sign_in/', views.sign_in, name='sign_in'),
    url(r'^sign_out/', views.sign_out, name='sign_out'),
]
