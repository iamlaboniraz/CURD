from django.db import models


# Create your models here.
class BookList(models.Model):
    """
     Don't use camelcase Field name
    """
    Title = models.CharField(max_length=150)
    Price = models.IntegerField()
    Author = models.CharField(max_length=100)

    def __str__(self):
        return self.Title
