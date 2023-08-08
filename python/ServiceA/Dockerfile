# syntax=docker/dockerfile:1

FROM python:3.9-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY *.py .

EXPOSE 5059

CMD ["python3", "-m" , "main", "run", "--host=0.0.0.0"]