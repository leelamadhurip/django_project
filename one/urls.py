from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('search/', views.search_movies, name='search'),
    path('add_movie_to_list/<str:imdb_id>/', views.add_movie_to_list, name='add_movie_to_list'),
    path('create_movie_list/', views.create_movie_list, name='create_movie_list'),
    #path('movie_lists/', views.movie_lists, name='movie_lists'),
    path('delete_movie_list/<int:list_id>/', views.delete_movie_list, name='delete_movie_list'),
    path('toggle_privacy/<int:list_id>/', views.toggle_privacy, name='toggle_privacy'),
    path('public/<int:list_id>/', views.view_public_list, name='view_public_list'),
]
