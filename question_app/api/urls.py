from django.urls import path

from question_app import views

urlpatterns = [
    # books
    path('books/', views.BookListAV.as_view(), name="books"),
    path('books/<int:pk>/', views.BookDetailAV.as_view(), name="book-detail"),
    # tags
    path('books/<int:pk>/tags/', views.TagListGV.as_view(), name="tags"),
    path('books/<int:pk>/tags/<int:pk2>/',
         views.TagDetailGV.as_view(), name="tag-detail"),
    path('books/<int:pk>/create-tag/',
         views.TagCreateGV.as_view(), name="create-tag"),
    # questions
    path('books/<int:pk>/create-question/',
         views.QuestionCreateGV.as_view(), name="create-question"),
    path('books/<int:pk>/tags/<int:pk2>/questions/',
         views.QuestionListGV.as_view(), name="questions-as-tag"),
    path('books/<int:pk>/tags/<int:pk2>/questions/<int:pk3>/',
         views.QuestionDetailGV.as_view(), name="question-detail"),
    path('books/<int:pk>/questions/',
         views.QuestionListAsBookGV.as_view(), name="questions-as-book"),
    # answers
    path('books/<int:pk>/tags/<int:pk2>/questions/<int:pk3>/answers/',
         views.AnswerListGV.as_view(), name="answers"),
    path('books/<int:pk>/tags/<int:pk2>/questions/<int:pk3>/answers/<int:pk4>/',
         views.AnswerDetailGV.as_view(), name="answer-detail"),
    path('books/<int:pk>/tags/<int:pk2>/questions/<int:pk3>/answer-create/',
         views.AnswerCreateGV.as_view(), name="create-answer"),
]
