FROM python:3.10-slim

RUN mkdir /app

COPY requeriment.txt /app

RUN pip3 install -r /app/requeriments.txt.txt --no-cache-dir

COPY ourjournal/ /app
WORKDIR /app
CMD ["python3", "manage.py", "runserver", "0:8000"]
