FROM python:3.9

RUN apt-get -y update

WORKDIR /usr/src/

COPY ./requirements.txt /usr/src/requirements.txt
COPY ./db /usr/src/db
COPY ./routers /usr/src/routers
COPY ./main.py /usr/src/main.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]


