from rest_framework.response import Response
from Library.models import BookInfo,Authors,Identyfires
from .serializers import BookInfoSerializer,AuthorsSerializer,IdentyfiresSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import filters

class BooksApiView(generics.ListCreateAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'language', 'publishedDate']

class AuthorApiView(generics.ListCreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class IdentyfiresApiView(generics.ListCreateAPIView):
    queryset = Identyfires.objects.all()
    serializer_class = IdentyfiresSerializer

class DocsView(APIView):
    def get(self,request):
            apidocs = {
                   'API Book List and Create': request.build_absolute_uri('api'),
                   'API Authors Create and List': request.build_absolute_uri('apiauthor'),
                   'API Identyfiers Create and List': request.build_absolute_uri('apiisbn')
                   }
            return Response(apidocs)