FROM python:3.13-slim

WORKDIR /code

COPY /requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app ./app

RUN addgroup  --system defaultgroup && adduser --system --group defaultuser

RUN chown -R defaultuser:defaultgroup /code

USER defaultuser

CMD ["fastapi", "run", "app/main.py", "--port", "80"]