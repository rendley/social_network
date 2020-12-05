from django.urls import path
from .views import PostView, GroupPostView, SearchView
app_name = 'posts'

urlpatterns = [

    path('', PostView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search_post'),
    path('group/<slug>/', GroupPostView.as_view(), name='group_post'),


]

