"""STXNext URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from Library.views import BookListView,AddBookView,AddGoogleBookView,main
from Library.api.views import BooksApiView,AuthorApiView,IdentyfiresApiView,DocsView

router = routers.DefaultRouter(trailing_slash=True)

urlpatterns = [
     path('books/', BookListView.as_view(),name = 'booklist'),
     path('books/addbook/',AddBookView.as_view(),name = 'addbook'),
     path('books/googlebook/', AddGoogleBookView.as_view(),name = 'googlebook'),
     path('api/', DocsView.as_view(),name = 'apilist'),
     path('api/books/',BooksApiView.as_view(), name = 'apibooklist'),
     path('api/author/',AuthorApiView.as_view(), name = 'apiauthorlist'),
     path('api/isbn/',IdentyfiresApiView.as_view(), name = 'apiisbnlist'),
     path('',main, name = 'main'),
]
urlpatterns += router.urls
