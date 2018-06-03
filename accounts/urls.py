
app_name = 'accounts'


from django.urls import path,include
from .views import signup



urlpatterns = [
    path('register/', signup, name='register'),
]