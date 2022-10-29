FROM python:3.8

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential


WORKDIR /home/demo
COPY ./app .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]