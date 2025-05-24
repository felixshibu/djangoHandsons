from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import MovieModel
from .serializers import MovieSerializer

# Create your views here.          
class MovieList (APIView):
    def get(self, request):
        if(request.query_params == {}):
            movies = MovieModel.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            genre =  request.query_params.get('genre')
            if not genre:
                return Response({"msg":"genre need to filter"},
                            status=status.HTTP_400_BAD_REQUEST)
            movies = MovieModel.objects.filter(genre=genre)
            if not movies.exists():
                return Response({"msg":"no data available"},
                                status=status.HTTP_400_BAD_REQUEST)
            serializer = MovieSerializer(movies, many=True)
            return Response (serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class MovieDetail(APIView):
    def get(self, request,pk):
        try:
            movies = MovieModel.objects.get(pk=pk)
            serializer = MovieSerializer(movies)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"msg":"movie object not found"},
                            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,pk):
        movie = MovieModel.objects.get(pk=pk)
        is_watched =  request.data.get("is_watched")
        if is_watched is None:
            return Response({"msg": "unable to update"},
                            status=status.HTTP_400_BAD_REQUEST)
        movie.is_watched = is_watched
        movie.save()
        serializer = MovieSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self, request,pk):
        movies = MovieModel.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)