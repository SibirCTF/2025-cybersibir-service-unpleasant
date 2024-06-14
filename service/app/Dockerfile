FROM python:3.11

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "db_init.py"]
#CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000"]
CMD ["flask", "--app", "app.py","run", "--host","0.0.0.0", "--port=5000"]
