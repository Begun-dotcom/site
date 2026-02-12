# 1. Используйте slim-образ для уменьшения размера
FROM python:3.13-slim


COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "app.main"]
