from rest_framework.response import Response
from Library.models import BookInfo,Authors,Identyfires
from .serializers import BookInfoSerializer,AuthorsSerializer,IdentyfiresSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import filters

class BooksApiView(generics.ListAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'language', 'publishedDate']
    ordering_fields = ['title', 'language', 'publishedDate']

class AuthorApiView(generics.ListAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

class IdentyfiresApiView(generics.ListAPIView):
    queryset = Identyfires.objects.all()
    serializer_class = IdentyfiresSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['identifier','type']

class DocsView(APIView):
    def get(self,request):
            apidocs = {
                   'API Book List and Create': request.build_absolute_uri('books/'),
                   'API Authors Create and List': request.build_absolute_uri('author'),
                   'API Identyfiers Create and List': request.build_absolute_uri('isbn')
                   }
            return Response(apidocs)