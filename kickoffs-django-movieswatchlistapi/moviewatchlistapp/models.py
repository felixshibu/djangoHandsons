from django.db import models

# Create your models here.
class MovieModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    is_watched = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
