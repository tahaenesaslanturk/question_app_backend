from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=150)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="tag_book")
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.TextField(max_length=1000)
    is_accepted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="question_book")
    tags = models.ManyToManyField(Tag, related_name="tags")
    hard_level = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)])

    def __str__(self) -> str:
        return "Question ID: " + str(self.id)


class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    is_true = models.BooleanField(default=False)

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="question")

    def __str__(self) -> str:
        return self.answer_text
