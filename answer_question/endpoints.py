from .models import Questions, Answers
from .serializers import QuestionsSerializer, AnswersSerializer
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, get_object_or_404

"QUESTION"

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


"ANSWERS"

class AnswerCreateAPIview(CreateAPIView):
    serializer_class = AnswersSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Answers.objects.all()

    def perform_create(self, serializer):
        question = get_object_or_404(Questions, pk=self.kwargs["pk"])
        serializer.save(question_id=question)


class AnswerRetrieveAPIView(RetrieveAPIView):
    serializer_class = AnswersSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Answers.objects.all()


class AnswerDeleteAPIView(DestroyAPIView):
    serializer_class = AnswersSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Answers.objects.all()
