from . import views
from django.urls import path


urlpatterns = [
    path('', views.sign, name='sign')
]
