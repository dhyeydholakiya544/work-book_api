from django.urls import path
from .views import *

urlpatterns = [
    path('', latestUpdateListAPI, name='latestUpdateListAPI'),
    path('latest-update/<int:update_id>', latestUpdateDetailAPI, name='latestUpdateDetailAPI')
]
