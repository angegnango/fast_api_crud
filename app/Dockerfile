FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ADD requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
ENV PYTHONPATH /app

RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 8000
