from django.conf.urls import url
from users import views
from users.views import SignIn, SignUp

# template tagging
app_name = 'users'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_up/', SignUp.as_view(), name='sign_up'),
    url(r'^sign_in/', SignIn.as_view(), name='sign_in'),
    url(r'^sign_out/', views.sign_out, name='sign_out'),
]
