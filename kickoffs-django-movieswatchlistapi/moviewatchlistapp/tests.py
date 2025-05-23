from django.test import TestCase, Client
from .models import MovieModel


class MovieWatchlistApi(TestCase):
    
    def setUp(self):
        
        self.client = Client()
        
        movie_data = [
                {"title": "Inception", "description": "A skilled thief leads a team into dreams to steal secrets.", "release_year": 2010, "genre": "Science Fiction", "is_watched": True },
                {"title":"The Godfather", "description": "An organized crime dynasty's aging patriarch transfers control to his reluctant son.", "release_year": 1972, "genre": "Crime", "is_watched": True },
                {"title": "Parasite", "description": "A poor family schemes to infiltrate a wealthy household.", "release_year": 2019, "genre": "Crime", "is_watched": False },
                {"title": "The Shawshank Redemption", "description": "Two imprisoned men bond over years, finding solace and redemption.", "release_year": 1994, "genre": "Drama", "is_watched": True }
            ]
        try:
            for movie in movie_data:
                m = MovieModel.objects.create(title=movie['title'], description=movie['description'], release_year=movie['release_year'], genre=movie['genre'], is_watched=movie['is_watched'])
        except Exception as e:
            print("Failed to initialise movie data : ", e)
        
    def test_01_moviedetails_post_ep_check(self):
        response = self.client.post('/movie')
        self.assertNotIn(response.status_code, [404, 405])

    def test_02_moviedetails_post_success(self):
        moviedata = [
                {"title": "Interstellar", "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.", "release_year": 2014, "genre": "Science Fiction", "is_watched": False },
                {"title":"The Dark Knight", "description": "Batman faces the Joker, a criminal mastermind who plunges Gotham into chaos.", "release_year": 2008, "genre": "Action", "is_watched": True}
            ]
        for data in moviedata:
            response = self.client.post('/movie', data=data)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json()['title'], data['title'])
            self.assertEqual(response.json()['release_year'], data['release_year'])
            self.assertEqual(response.json()['genre'], data['genre'])
    
    def test_03_moviedetails_get_ep_check(self):
        response = self.client.get('/movie')
        self.assertNotIn(response.status_code, [404, 405])

    def test_04_moviedetails_get_success(self):
        response = self.client.get('/movie?genre=Crime')
        self.assertEqual(response.status_code, 200) 
        self.assertGreaterEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]["title"], "The Godfather")
        self.assertEqual(response.json() [1] ['release_year'], 2019)
        self.assertEqual(response.json()[0]['genre'], 'Crime')

    def test_05_moviedetails_patch_success (self): 
        moviedetail_data = {"is_watched": False}
        response = self.client.patch('/movie/1', data=moviedetail_data, content_type="application/json")
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.json()['is_watched'], False)
    
    def test_06_moviedetails_patch_error(self):
        response = self.client.patch('/movie/2')
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response.json()['msg'], "unable to update")
    
    def test_07_moviedetails_delete_success (self):
        response = self.client.delete('/movie/4')
        self.assertEqual(response.status_code, 204)