from django.db import models
from .validators import MinYearValidator, MaxYearValidator,MinPagesValidator

# Create your models here.
ISBN = [(0,'ISBN-10'),
        (1,'ISBN-13')]

class Identyfires(models.Model):
    type = models.IntegerField()
    identifier = models.IntegerField()

class BookInfo(models.Model):
    title = models.TextField
    authors = models.TextField()
    publishedDate = models.IntegerField(validators=[MinYearValidator,MaxYearValidator])
    industryIdentifiers = models.ForeignKey(Identyfires,on_delete=models.CASCADE)
    pageCount=models.IntegerField(validators=[MinPagesValidator])
    imageLinks = models.TextField()
    language = models.TextField()