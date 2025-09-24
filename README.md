# test_api_service

API-сервис приложение (Django, DRF), реализующее логику вопросов и ответов:
- Создание и получение вопросов и ответов
- Добавление и удаление
- Есть связь ответов с пользователями

Стек:
- Python 3.10
- Django 5.x
- DRF
- PostgreSQL
- Docker, docker-compose
- Poetry (управление зависимостями)

Установка и запуск:
1. Клонирование репозитория
- git clone git@github.com:Valkirik/test_api_service.git
- cd test_api_service

*В моем случае .env в не в git ignore, поэтому создавать ненужно*

2. Запуск сервера
- docker compose build
- docker compose up
- docker compose exec web python manage.py createsuperuser   
