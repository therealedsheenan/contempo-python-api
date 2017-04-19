from django.conf.urls import url
from first_app.views import Index

# template tagging
app_name = 'first_app'

urlpatterns = [
  url(r'^$', Index.as_view()),
]
