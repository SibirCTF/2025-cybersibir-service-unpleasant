FROM python:3.11

WORKDIR /service

COPY ./requirements.txt /service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /service/requirements.txt

COPY ./app /service/app

EXPOSE 5000

CMD ["python", "app/db_init.py"]
CMD ["flask", "--app", "app/app.py","run", "--host","0.0.0.0", "--port=5000"]
