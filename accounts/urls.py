
app_name = 'accounts'


from django.urls import path,include
from .views import RegisterView,guest_register_view,LoginView


urlpatterns = [
 path('register/',RegisterView.as_view(),name='register'),
 path('register/guest/',guest_register_view,name='guest_register'),
 path('login/',LoginView.as_view(),name='login'),
]