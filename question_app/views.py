from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status, filters
from rest_framework.response import Response

from question_app.models import (Book, Tag, Question, Answer)
from question_app.api import (serializers, permissions)


# BOOK VIEWS
class BookListAV(APIView):

    permission_classes = [permissions.AdminOrReadOnly]

    def get(self, request):
        books = Book.objects.all()
        serializer = serializers.BookSerializer(
            books, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class BookDetailAV(APIView):
    permission_classes = [permissions.AdminOrReadOnly]

    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book Is Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = serializers.BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requst, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# TAG VIEWS


class TagListGV(generics.ListAPIView):
    serializer_class = serializers.TagSerializer
    permission_classes = [permissions.AdminOrReadOnly]
    filter_backends = [
        filters.SearchFilter, filters.OrderingFilter]

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Tag.objects.filter(book=pk)


class TagDetailGV(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = [permissions.AdminOrReadOnly]
    lookup_url_kwarg = "pk2"
    lookup_field = "id"

    def get_queryset(self):
        book_id = self.kwargs["pk"]
        tag_id = self.kwargs["pk2"]
        return Tag.objects.filter(book=book_id, id=tag_id)


class TagCreateGV(generics.CreateAPIView):
    serializer_class = serializers.TagSerializer
    permission_classes = [permissions.AdminOrReadOnly]

    def get_queryset(self):
        return Tag.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        book = Book.objects.get(pk=pk)
        serializer.save(book=book)

# QUESTION VIEWS


class QuestionListGV(generics.ListAPIView):
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.AdminOrReadOnly]
    filter_backends = [
        filters.SearchFilter, filters.OrderingFilter]

    def get_queryset(self):
        pk = self.kwargs["pk2"]
        return Question.objects.filter(tags__id=pk)


class QuestionListAsBookGV(generics.ListAPIView):
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.AdminOrReadOnly]
    filter_backends = [
        filters.SearchFilter, filters.OrderingFilter]

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Question.objects.filter(book=pk)


class QuestionDetailGV(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.AdminOrReadOnly]

    lookup_url_kwarg = "pk3"
    lookup_field = "id"

    def get_queryset(self):
        book_id = self.kwargs["pk"]
        tag_id = self.kwargs["pk2"]
        question_id = self.kwargs["pk3"]
        return Question.objects.filter(book=book_id, id=question_id, tags__id=tag_id)


class QuestionCreateGV(generics.CreateAPIView):
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.AdminOrReadOnly]

    def get_queryset(self):
        return Question.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        book = Book.objects.get(pk=pk)
        serializer.save(book=book)

# ANSWER VIEWS


class AnswerListGV(generics.ListAPIView):
    serializer_class = serializers.AnswerSerializer
    permission_classes = [permissions.AdminOrReadOnly]
    filter_backends = [
        filters.SearchFilter, filters.OrderingFilter]

    def get_queryset(self):
        pk = self.kwargs["pk3"]
        return Answer.objects.filter(question=pk)


class AnswerDetailGV(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    permission_classes = [permissions.AdminOrReadOnly]

    lookup_url_kwarg = "pk4"
    lookup_field = "id"

    def get_queryset(self):

        answer_id = self.kwargs["pk4"]
        return Answer.objects.filter(id=answer_id)


class AnswerCreateGV(generics.CreateAPIView):
    serializer_class = serializers.AnswerSerializer
    permission_classes = [permissions.AdminOrReadOnly]

    def get_queryset(self):
        return Answer.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk3')
        question = Question.objects.get(pk=pk)
        # max 5 answer
        if Answer.objects.filter(question=question).count() < 5:
            serializer.save(question=question)
