FROM python:3.8-alpine
RUN mkdir /code
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "main.py"]