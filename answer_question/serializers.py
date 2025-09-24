from rest_framework.serializers import ModelSerializer

from .models import Questions, Answers


class QuestionsSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"


class AnswersSerializer(ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"