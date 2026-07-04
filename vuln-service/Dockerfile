FROM python:3.11-alpine

WORKDIR /service

COPY ./requirements.txt /service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /service/requirements.txt

COPY ./app /service/app

EXPOSE 5000

CMD ["flask", "--app", "app/app.py","run", "--host","0.0.0.0", "--port=5000"]
