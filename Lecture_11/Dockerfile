FROM python:3.8

WORKDIR /Lecture_11

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .
CMD ["python", "./server.py"]