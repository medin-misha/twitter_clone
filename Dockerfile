FROM python:3.12

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY alembic/ app/alembic
COPY alembic.ini /app/
COPY core /app/core
COPY handlers /app/handlers
COPY tests /app/tests
COPY main.py /app/
COPY static /app/static/

ENV db_url postgresql+asyncpg://postgres_user:postgres_password@192.168.5.194:5432/postgres_db
ENV image_saver_url http://192.168.5.194:9000/

WORKDIR /app
RUN alembic upgrade head
CMD ["gunicorn", "main:app", "--workers", "2",  "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]

