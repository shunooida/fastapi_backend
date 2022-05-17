FROM python:3.9

RUN apt-get -y update

WORKDIR /usr/src/

COPY ./apps /usr/src/apps
COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /usr/src/apps

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]


