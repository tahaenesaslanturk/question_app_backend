from django.db.models import fields
from question_app import models
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Book
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        exclude = ["is_accepted"]


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        exclude = ["is_accepted", "book"]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Answer
        exclude = ["question"]
