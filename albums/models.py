from django.db import models
from musician_profile.models import Musician


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField(auto_now_add=True)
    Choices = [(i, str(i)) for i in range(1, 6)]
    rating = models.IntegerField(choices=Choices, default=5, max_length=2)

    def __str__(self):
        return f"{self.name} | {self.musician} | {self.release_date}"
