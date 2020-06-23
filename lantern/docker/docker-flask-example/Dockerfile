FROM python:3-alpine

LABEL email="email@gmail.com"

COPY /app /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]