from django.urls import path
from .views import PostView, GroupPostView
app_name = 'posts'

urlpatterns = [
    path('/group/<slug>/', GroupPostView.as_view(), name='group_post'),
    path('', PostView.as_view(), name='index'),


]

