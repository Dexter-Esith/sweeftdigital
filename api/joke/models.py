from django.db import models

# Create your models here.
class Joke(models.Model):
    author = models.CharField(max_length=100, null=True)
    joke = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.joke)