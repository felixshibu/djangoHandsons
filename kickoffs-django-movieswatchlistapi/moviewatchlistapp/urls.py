from django.urls import path
from .views import MovieDetail,MovieGenreList,MovieList


urlpatterns = [
    path('movie/', MovieList.as_view(),name='movie list'),
    path('movie/<int:pk>/',MovieDetail.as_view(),name='movie_detail'),
    path('movie/<str:genre>',MovieGenreList.as_view(),name='movie_genre_list')
]