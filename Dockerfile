FROM python:3.8
WORKDIR /home/demo
COPY ./app .
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python3", "wsgi.py"]