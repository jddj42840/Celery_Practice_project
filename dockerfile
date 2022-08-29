FROM python:3.9.10-alpine3.15
WORKDIR /test-project
COPY requirements.txt /test-project/.
RUN pip install -r requirements.txt
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV CELERY_BROKER_URL redis://cache:6379/0
EXPOSE 5000
ENV HOST 0.0.0.0
ENV DEBUG true
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--preload"]

