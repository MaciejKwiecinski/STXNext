from django.db import models
from .validators import MinPagesValidator
# Create your models here.

class BookInfo(models.Model):
    title = models.TextField(blank = True)
    publishedDate = models.TextField(blank = True)
    pageCount=models.IntegerField(validators=[MinPagesValidator],blank = True)
    imageLinks = models.TextField(blank = True)
    language = models.TextField(blank = True)

class Authors(models.Model):
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    name = models.TextField(blank = True)

    def __str__(self):
        return self.name

class Identyfires(models.Model):
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    type = models.CharField(max_length=250,blank = True)
    identifier = models.CharField(max_length=250,blank = True)
