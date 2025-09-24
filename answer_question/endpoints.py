from .models import Questions, Answers
from .serializers import QuestionsSerializer, AnswersSerializer
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Questions.objects.all()


class QuestionCreateAPIView(CreateAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Questions.objects.all()


class QuestionRetrieveAPIView(RetrieveAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Questions.objects.all()


class QuestionDeleteAPIView(DestroyAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Questions.objects.all()
