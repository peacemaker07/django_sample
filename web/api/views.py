from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from .models import Book
from .serializer import BookSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookBulkView(generics.UpdateAPIView):

    lookup_field = 'id'
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def put(self, request, *args, **kwargs):

        books = request.data



        return Response(status=status.HTTP_200_OK)
