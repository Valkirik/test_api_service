from django.urls import path
from .endpoints import QuestionListAPIView, QuestionCreateAPIView, QuestionRetrieveAPIView, QuestionDeleteAPIView

urlpatterns = [
    path("list_question/", QuestionListAPIView.as_view()),
    path("create_question/", QuestionCreateAPIView.as_view()),
    path("question/<int:pk>/delete/", QuestionDeleteAPIView.as_view()),
    path("get_question/<int:pk>/", QuestionRetrieveAPIView.as_view())
]