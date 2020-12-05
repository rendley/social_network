from django.urls import path
from .views import SignUp, ContactView
app_name = 'users'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('contact/', ContactView.as_view(), name='contact'),



]