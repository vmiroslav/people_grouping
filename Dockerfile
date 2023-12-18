FROM python:3.12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN pip install --upgrade pip  

COPY requiremets.txt  .

RUN pip install -r requiremets.txt

COPY . .

EXPOSE 8000  

CMD python manage.py migrate