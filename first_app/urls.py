from django.conf.urls import url
from first_app.views import IndexView

# template tagging
app_name = 'first_app'

urlpatterns = [
  url(r'^$', IndexView.as_view(), name='index'),
]
