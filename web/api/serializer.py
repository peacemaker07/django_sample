from rest_framework import serializers

from .models import Book, Content


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ('id', 'content')


class BookSerializer(serializers.ModelSerializer):

    contents = ContentSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'is_display', 'contents')
