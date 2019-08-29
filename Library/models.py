from django.db import models
from .validators import MinYearValidator, MaxYearValidator,MinPagesValidator,ISBNValidator
# Create your models here.
ISBN = [(0,'ISBN-10'),
        (1,'ISBN-13')]

class Authors(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Identyfires(models.Model):
    type = models.IntegerField(choices=ISBN)
    identifier = models.BigIntegerField(validators=[ISBNValidator])


class BookInfo(models.Model):
    title = models.TextField()
    authors = models.ForeignKey(Authors,on_delete=models.CASCADE)
    publishedDate = models.IntegerField(validators=[MinYearValidator,MaxYearValidator])
    industryIdentifiers = models.ForeignKey(Identyfires,on_delete=models.CASCADE)
    pageCount=models.IntegerField(validators=[MinPagesValidator])
    imageLinks = models.TextField()
    language = models.TextField()

