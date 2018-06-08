
app_name = 'accounts'


from django.urls import path,include
from .views import register_view,guest_register_view,login_view


urlpatterns = [
 path('register/',register_view,name='register'),
 path('register/guest/',guest_register_view,name='guest_register'),
 path('login/',login_view,name='login'),
]