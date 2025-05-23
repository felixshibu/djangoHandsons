from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import MovieModel
from .serializers import MovieSerializer

# Create your views here.
class MovieGenreList (APIView):
    def get(self, request, genre):
        if(genre == ''):
            return Response({"error":"genre need to filter"},
                        status=status.HTTP_400_BAD_REQUEST)
        try:
            movies = MovieModel.objects.filter(genre=genre)
            serializer = MovieSerializer(movies, many=True)
            return Response (serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error":"no data available"},
                        status=status.HTTP_400_BAD_REQUEST)
            
class MovieList (APIView):
    def get(self, request):
        movies = MovieModel.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

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
            serializer = MovieSerializer(movies,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error":"movie object not found"},
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk):
        movie = MovieModel.object.get(pk=pk)
        serializer = MovieSerializer(movie,data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"error":"unable to update"},
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        movies = MovieModel.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)

