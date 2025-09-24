from django.db import models
from .mixins import DataTimeMixin
from django.contrib.auth.models import User


class Questions(DataTimeMixin):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text


class Answers(DataTimeMixin):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return self.text


