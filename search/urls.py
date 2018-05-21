app_name = 'search'

from django.urls import path, include
from .views import SearchProductView


app_name = 'products'
urlpatterns = [
    path('', SearchProductView.as_view(), name='list'),
]
