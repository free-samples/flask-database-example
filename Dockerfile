FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
# CMD ["tail", "-f", "requirements.txt"]