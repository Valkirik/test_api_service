import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from answer_question.models import Questions, Answers

@pytest.mark.django_db
def test_question_list():
    q1 = Questions.objects.create(text="The first question?")
    q2 = Questions.objects.create(text="The second question?")

    client = APIClient()
    url = reverse("question-list-create")
    resp = client.get(url)

    assert resp.status_code == status.HTTP_200_OK
    assert isinstance(resp.data, list)
    texts = [item["text"] for item in resp.data]
    assert q1.text in texts and q2.text in texts

