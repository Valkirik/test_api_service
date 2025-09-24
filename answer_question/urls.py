from django.urls import path
from .endpoints import QuestionListAPIView, QuestionCreateAPIView, QuestionRetrieveAPIView,\
    QuestionDeleteAPIView, AnswerCreateAPIview, AnswerRetrieveAPIView, AnswerDeleteAPIView



urlpatterns = [
    path("list_question/", QuestionListAPIView.as_view()),
    path("create_question/", QuestionCreateAPIView.as_view()),
    path("question/<int:pk>/delete/", QuestionDeleteAPIView.as_view()),
    path("get_question/<int:pk>/", QuestionRetrieveAPIView.as_view()),
    path("get_answer/<int:pk>/", AnswerRetrieveAPIView.as_view()),
    path("answer/<int:pk>/delete/", AnswerDeleteAPIView.as_view()),
    path("create_answer/", AnswerCreateAPIview.as_view()),
]