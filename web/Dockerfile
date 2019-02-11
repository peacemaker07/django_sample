FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/django_sample/static
RUN mkdir /var/log/django_sample
RUN touch /var/log/django_sample/products.log
WORKDIR /usr/src/django_sample
COPY . /usr/src/django_sample/
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
