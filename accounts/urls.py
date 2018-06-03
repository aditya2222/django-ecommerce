
app_name = 'accounts'


from django.urls import path,include
from .views import CreateUserView



urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
]