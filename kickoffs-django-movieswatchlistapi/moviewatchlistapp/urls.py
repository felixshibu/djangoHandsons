from django.urls import path
from .views import MovieDetail,MovieList

urlpatterns = [
    path('movie', MovieList.as_view(),name='movie list'),
    path('movie/<int:pk>',MovieDetail.as_view(),name='movie_detail'),
]