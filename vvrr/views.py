from django.shortcuts import render
# from rest_framework import generics,mixins
from .models import Books, Genre
from .serializers import BookSerializer, GenreSerializer
from rest_framework import viewsets

# Create your views here.
# class BooksView1(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
#     serializer_class = BookSerializer
#     queryset = Books.objects.all()
    
#     def post(self, request):
#         return self.create(request)
#     def get(self, request):
#         return self.list(request)

# class BooksView2(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
#     serializer_class = BookSerializer
#     queryset = Books.objects.all()
#     lookup_field = 'id'

#     def get(self, request, id):
#         return self.retrieve(request, id)
#     def patch(self, request, id):
#         return self.partial_update(request,id)
#     def put(self, request, id):
#         return self.update(request, id)
#     def delete(self, request, id):
#         return self.destroy(request, id)

# class GenreView1(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
#     serializer_class = GenreSerializer
#     queryset = Genre.objects.all()
    
#     def post(self, request):
#         return self.create(request)
#     def get(self, request):
#         return self.list(request)

# class GenreView2(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
#     serializer_class = GenreSerializer
#     queryset = Genre.objects.all()
#     lookup_field = 'id'

#     def get(self, request, id):
#         return self.retrieve(request, id)
#     def patch(self, request, id):
#         return self.partial_update(request,id)
#     def put(self, request, id):
#         return self.update(request, id)
#     def delete(self, request, id):
#         return self.destroy(request, id)


class BooksView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()

class GenreView(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()