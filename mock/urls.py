from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mocked-data/$', views.MockData.as_view(), name='mocked-data'),
]