FROM python:3.9-slim

COPY . /app

ADD requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]