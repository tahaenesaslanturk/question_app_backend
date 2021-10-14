from django.contrib import admin

from question_app.models import Book, Tag, Question, Answer


class TagAdmin(admin.ModelAdmin):
    list_filter = ("is_accepted", "book",)
    list_display = ("name", "book", "is_accepted",)


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ("is_accepted", "book",)
    list_display = ("id", "question_text", "book", "is_accepted",)


class AnswerAdmin(admin.ModelAdmin):
    list_filter = ("is_true", "question",)
    list_display = ("answer_text", "is_true", "question",)


admin.site.register(Book)
admin.site.register(Tag, TagAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
