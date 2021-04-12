from django.urls import path
from .import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:id>/', views.detail, name="detail"),
    path('addmovies/', views.add_movies, name="add_movies"),
    path('editmovies/<int:id>/', views.edit_movies, name="edit_movies"),
    path('deletemovies/<int:id>/', views.delete_movies, name="delete_movie"),
    path('addreview/<int:id>/', views.add_review, name="add_review")
]

