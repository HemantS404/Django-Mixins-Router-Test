from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import BooksView1, BooksView2, GenreView1, GenreView2
from .views import BooksView,GenreView

router = DefaultRouter()
router.register('books', BooksView, 'book-view')
router.register('genre', GenreView, 'genre-view')

urlpatterns = [
    path('', include(router.urls))
    # path('books/', BooksView1.as_view(), name = 'book-view-1'),
    # path('books/<id>/', BooksView2.as_view(), name ='book-view-2'),
    # path('genre/', GenreView1.as_view(), name  = 'genre-view-1'),
    # path('genre/<id>/', GenreView2.as_view(), name  = 'genre-view-2'),
]