FROM python:3.8.18-slim

WORKDIR /app

COPY ./requirements.txt /app

RUN  pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

EXPOSE 3001/tcp

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "3001"]



