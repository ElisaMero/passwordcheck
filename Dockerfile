FROM python:3

RUN python3 -m venv venv

COPY . . 

RUN pip install flask

EXPOSE 5000

CMD flask run --host=0.0.0.0


