from django.db import models
from .validators import MinYearValidator, MaxYearValidator,MinPagesValidator,ISBN10Validator,ISBN13Validator

# Create your models here.
ISBN = [(0,'ISBN-10'),
        (1,'ISBN-13')]

class Authors(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Identyfires(models.Model):
    type = models.IntegerField()
    identifier = models.IntegerField(validators=[ISBN10Validator,ISBN13Validator])


class BookInfo(models.Model):
    title = models.TextField()
    authors = models.ForeignKey(Authors,on_delete=models.CASCADE)
    publishedDate = models.IntegerField(validators=[MinYearValidator,MaxYearValidator])
    industryIdentifiers = models.ForeignKey(Identyfires,on_delete=models.CASCADE)
    pageCount=models.IntegerField(validators=[MinPagesValidator])
    imageLinks = models.TextField()
    language = models.TextField()

