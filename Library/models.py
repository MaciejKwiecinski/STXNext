from django.db import models
from .validators import MinPagesValidator
# Create your models here.

class BookInfo(models.Model):
    title = models.TextField()
    publishedDate = models.DateField(blank = True)
    pageCount=models.IntegerField(validators=[MinPagesValidator])
    imageLinks = models.TextField()
    language = models.TextField()

class Authors(models.Model):
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name

class Identyfires(models.Model):
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    type = models.CharField(max_length=7)
    identifier = models.CharField(max_length=13)
